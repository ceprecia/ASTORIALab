#!/usr/bin/env node
// Local static application analysis entry point. Built from the pinned source.
import { readFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { once } from 'node:events';
import { analyzeJavaScriptApplication } from '@rea-source/application/javascript/JavaScriptApplicationService.js';
import { ArtifactResourceScope } from '@rea-source/artifacts/ArtifactResourceScope.js';
import { inspectAnalysisView } from '@rea-source/application/analysisView/AnalysisViewService.js';
import { bufferedJsonParts, jsonParts } from '@rea-source/domain/jsonSerialization.js';

const version = '6.5.0-local.1';
const help = [
  'REA local ' + version,
  'analyze-javascript-application ABS_PATH --json',
  'inspect-analysis-view INPUT_JSON_OR_FILE --json',
  '--help',
  '--version',
].join('\n');

async function writeJson(value) {
  for (const part of bufferedJsonParts(jsonParts(value))) {
    if (!process.stdout.write(part)) await once(process.stdout, 'drain');
  }
  process.stdout.write('\n');
}

function describeError(error, depth = 0) {
  const result = {
    type: error?._tag || error?.name || 'Error',
    message: error?.message || String(error),
  };
  if (typeof error?.reason === 'string') result.reason = error.reason;
  if (error?.cleanup) result.cleanup = error.cleanup;
  if (Array.isArray(error?.issues)) result.issues = error.issues;
  if (error?.diagnostics) result.diagnostics = error.diagnostics;
  if (error?.capturedOutput) result.captured_output = error.capturedOutput;
  if (depth < 5 && error?.cause) result.cause = describeError(error.cause, depth + 1);
  if (depth < 5 && Array.isArray(error?.errors)) {
    result.errors = error.errors.map((item) => describeError(item, depth + 1));
  }
  return result;
}

function errorResult(error) {
  return { error: describeError(error) };
}

async function run() {
  const args = process.argv.slice(2);
  if (args.length === 1 && args[0] === '--version') {
    process.stdout.write(version + '\n');
    return;
  }
  if (args.length === 0 || (args.length === 1 && args[0] === '--help')) {
    process.stdout.write(help + '\n');
    return;
  }
  if (args.length !== 3 || args[2] !== '--json' || args[1].startsWith('--')) {
    throw new Error('Use one supported command, one input, and --json.');
  }
  const [command, input] = args;
  let result;
  if (command === 'analyze-javascript-application') {
    const resources = new ArtifactResourceScope();
    let cleanupError;
    const controller = new AbortController();
    const stop = () => controller.abort(new Error('Analysis cancelled'));
    process.once('SIGINT', stop);
    process.once('SIGTERM', stop);
    try {
      result = await analyzeJavaScriptApplication(
        { input_path: resolve(input) }, resources, { signal: controller.signal },
      );
    } finally {
      process.removeListener('SIGINT', stop);
      process.removeListener('SIGTERM', stop);
      try { await resources.close(); } catch (error) { cleanupError = error; }
    }
    if (cleanupError) {
      throw new AggregateError(result && !result.ok ? [result.error, cleanupError] : [cleanupError],
        'Static analysis cleanup failed');
    }
  } else if (command === 'inspect-analysis-view') {
    let value;
    if (input.trimStart().startsWith('{')) value = JSON.parse(input);
    else value = JSON.parse(await readFile(resolve(input), 'utf8'));
    if (value?.source?.kind !== 'inline') {
      throw new Error('Supply the complete saved Evidence in source.kind=inline.');
    }
    result = inspectAnalysisView(value);
  } else {
    throw new Error('Unsupported command: ' + command);
  }
  if (!result.ok) {
    process.exitCode = 1;
    await writeJson(errorResult(result.error));
    return;
  }
  await writeJson(result.value);
}

try {
  await run();
} catch (error) {
  process.exitCode = 1;
  await writeJson(errorResult(error));
}
