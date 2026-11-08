// Compile only the local entry point and its parser worker from source.
import { readFile, mkdir, writeFile } from 'node:fs/promises';
import { join, resolve } from 'node:path';
import { createRequire } from 'node:module';

const [sourceRoot, runtimeRoot, dependencyRoot, entrypoint] = process.argv.slice(2);
const require = createRequire(join(dependencyRoot, 'package.json'));
const { build } = require('esbuild');
const source = resolve(sourceRoot, 'src');
const staticReader = [
  'export const createReader = (path, format) => {',
  '  if (format === "directory") return new DirectoryArtifactReader(path);',
  '  if (format === "asar") return new AsarArtifactReader(path);',
  '  return undefined;',
  '};',
  '',
].join('\n');
const plugin = {
  name: 'local-static-runtime',
  setup(context) {
    context.onResolve({ filter: /^@electron\/asar$/ }, () => ({
      path: resolve(entrypoint, '../asar_header.mjs'),
    }));
    context.onResolve({ filter: /^@rea-source\// }, ({ path }) => ({
      path: join(source, path.slice('@rea-source/'.length).replace(/\.js$/, '.ts')),
    }));
    context.onLoad({ filter: /[\\/]src[\\/].*\.ts$/ }, async ({ path }) => {
      let contents = await readFile(path, 'utf8');
      if (path.endsWith('/artifacts/inventory/reader.ts')) {
        contents = contents.replace(/^import \{ (MachOSliceArtifactReader|NativeDmgArtifactReader|ZipArtifactReader) \}[^\n]*\n/gm, '');
        const start = contents.indexOf('export const createReader =');
        const end = contents.indexOf('/** Decide traversal scope', start);
        if (start < 0 || end < 0) throw new Error('Static reader adaptation no longer matches');
        contents = contents.slice(0, start) + staticReader + contents.slice(end);
      }
      if (path.endsWith('/process/DarwinProcessRunTokenReader.ts')) {
        contents = contents.replaceAll('../../bridge/process/', '../bridge/process/');
      }
      if (path.endsWith('/javascript/analysis/JavaScriptAnalysisWorker.ts')) {
        contents = contents.replace(/^import \{ cleanupOwnedProcessGroup \}[^\n]*\n/m, '');
        contents = contents.replace(/^import \{ prepareProcessOwnershipInspection \}[^\n]*\n/m, '');
        contents = contents.replace('await prepareProcessOwnershipInspection(signal);', 'signal?.throwIfAborted();');
        const cleanup = /\s*cleanup:\s*spawned\.cleanup \?\?\s*\(\(\) => cleanupOwnedProcessGroup\(spawned\.ownership\)\),/;
        if (!cleanup.test(contents)) throw new Error('Worker lifecycle adaptation no longer matches');
        contents = contents.replace(cleanup, '');
      }
      if (path.endsWith('/process/ProviderProcess.ts')) {
        contents = contents.replace(/^import \{ WindowsOwnedProcess \}[^\n]*\n/m, '');
        contents = contents.replace(/import \{\s*prepareProcessOwnershipInspection,\s*systemProcessOwnershipHost,\s*\} from "\.\/ProcessOwnershipObservation\.js";\n/, '');
        const start = contents.indexOf('export const spawnOwnedProviderProcess = async (');
        const end = contents.indexOf('/**\n * Supervises only generic process resources', start);
        if (start < 0 || end < 0) throw new Error('Parser launcher adaptation no longer matches');
        const launcher = [
          'export const spawnOwnedProviderProcess = async (options) => {',
          '  options.signal?.throwIfAborted();',
          '  const child = spawn(options.command, [...options.arguments], {',
          '    shell: false, stdio: ["pipe", "pipe", "pipe"],',
          '    env: {...options.hostEnvironment, ...options.env}, cwd: options.cwd,',
          '  });',
          '  await new Promise((resolve, reject) => { child.once("spawn", resolve); child.once("error", reject); });',
          '  return {process: child};',
          '};',
          '',
        ].join('\n');
        contents = contents.slice(0, start) + launcher + contents.slice(end);
      }
      return { contents, loader: 'ts' };
    });
  },
};

await mkdir(join(runtimeRoot, 'bin'), { recursive: true });
await mkdir(join(runtimeRoot, 'lib'), { recursive: true });
const common = {
  bundle: true, platform: 'node', format: 'esm', target: 'node22',
  nodePaths: [join(dependencyRoot, 'node_modules')],
  treeShaking: true, minifyIdentifiers: true, minifyWhitespace: true,
  legalComments: 'inline', metafile: true, logLevel: 'error', plugins: [plugin],
  banner: { js: "import { createRequire as __localRequire } from 'node:module'; const require = __localRequire(import.meta.url);" },
};
const outputs = [];
outputs.push(await build({ ...common, entryPoints: [entrypoint], outfile: join(runtimeRoot, 'bin/rea.mjs') }));
outputs.push(await build({ ...common, entryPoints: [join(source, 'composition/javascriptAnalysisWorkerProcess.ts')], outfile: join(runtimeRoot, 'lib/javascript_worker.mjs') }));
const inputs = [...new Set(outputs.flatMap((result) => Object.keys(result.metafile.inputs)))].sort();
await writeFile(join(dependencyRoot, 'bundle_inputs.json'), JSON.stringify(inputs, null, 2) + '\n');
process.stdout.write(JSON.stringify({ inputs: inputs.length, outputs: ['bin/rea.mjs', 'lib/javascript_worker.mjs'] }) + '\n');
