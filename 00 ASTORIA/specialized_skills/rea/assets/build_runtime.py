#!/usr/bin/env python3
"""Build and verify the pinned local REA static runtime.

Python standard library, Node 22.19+/24.11+/26+, and npm are required.
Build: python build_runtime.py build --source-root SOURCE --runtime-root OUTPUT
Check: python build_runtime.py verify --runtime-root OUTPUT
The caller verifies and extracts the source archive using runtime_spec.json.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import struct
import subprocess
import sys
import tempfile


ASSETS = Path(__file__).resolve().parent
VERSION = '6.5.0-local.1'
COMMANDS = ['analyze-javascript-application', 'inspect-analysis-view']
SOURCE_VERSION = '6.5.0'


def run_command(arguments, *, cwd=None, env=None, timeout=360):
    result = subprocess.run(arguments, cwd=cwd, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    if result.returncode != 0:
        raise RuntimeError('Command failed: ' + arguments[0] + '\n' + result.stderr[-6000:]
                           + '\n' + result.stdout[-2000:])
    return result


def check_node():
    observed = run_command(['node', '--version']).stdout.strip().lstrip('v')
    version = tuple(int(part) for part in observed.split('.')[:3])
    supported = ((22, 19, 0) <= version < (23, 0, 0)
                 or (24, 11, 0) <= version < (25, 0, 0)
                 or version >= (26, 0, 0))
    if not supported:
        raise RuntimeError('Unsupported Node version: ' + observed)


def check_assets():
    specification = json.loads((ASSETS / 'runtime_spec.json').read_text())
    if hashlib.sha256(Path(__file__).read_bytes()).hexdigest() != specification['recipe']['sha256']:
        raise RuntimeError('Build recipe changed')
    for item in specification['recipe']['inputs']:
        path = ASSETS / item['path']
        if hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
            raise RuntimeError('Build input changed: ' + item['path'])


def build(source_root, runtime_root, offline=False):
    check_node()
    check_assets()
    source_root = source_root.resolve()
    runtime_root = runtime_root.resolve()
    if json.loads((source_root / 'package.json').read_text())['version'] != SOURCE_VERSION:
        raise RuntimeError('Source version does not match the pinned release')
    specification = json.loads((ASSETS / 'runtime_spec.json').read_text())
    for item in specification['source']['files']:
        path = source_root / item['path']
        if hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
            raise RuntimeError('Pinned source file changed: ' + item['path'])
    if runtime_root.exists() and any(runtime_root.iterdir()):
        raise RuntimeError('Build output must be an empty candidate directory')
    runtime_root.mkdir(parents=True, exist_ok=True)
    # Dependencies and build metadata are temporary and never enter the runtime.
    with tempfile.TemporaryDirectory(prefix='rea_local_build_', dir=source_root.parent) as directory:
        dependency_root = Path(directory)
        shutil.copyfile(ASSETS / 'runtime_package.json', dependency_root / 'package.json')
        shutil.copyfile(ASSETS / 'runtime_package_lock.json', dependency_root / 'package-lock.json')
        environment = os.environ.copy()
        environment['npm_config_cache'] = str(dependency_root / 'npm_cache')
        environment['npm_config_update_notifier'] = 'false'
        environment['NO_UPDATE_NOTIFIER'] = '1'
        arguments = ['npm', 'ci', '--ignore-scripts', '--no-audit', '--no-fund']
        if offline:
            arguments.append('--offline')
        run_command(arguments, cwd=dependency_root, env=environment)
        run_command(['node', str(ASSETS / 'bundle_runtime.mjs'), str(source_root),
                     str(runtime_root), str(dependency_root), str(ASSETS / 'local_cli.mjs')],
                    cwd=dependency_root, env=environment)
        inputs = json.loads((dependency_root / 'bundle_inputs.json').read_text())
        forbidden = ['/node_modules/incur/', '/node_modules/pino/', '/node_modules/turbo/',
                     '/node_modules/@modelcontextprotocol/', '/src/mcp/', '/src/cli/',
                     '/src/cliLogging.', '/src/logger.', '/src/application/Update',
                     '/src/application/Setup', '/src/hopper/', '/src/ghidra/',
                     '/src/ida/', '/src/browser/', '/src/frida/']
        for path in inputs:
            if any(fragment in path for fragment in forbidden):
                raise RuntimeError('Excluded source entered the runtime: ' + path)
    # This import maps only to a standard-input parser worker, not a listener.
    package = {'name': 'rea-local', 'version': VERSION, 'private': True, 'type': 'module',
               'imports': {'#javascript-analysis-worker': './lib/javascript_worker.mjs'}}
    (runtime_root / 'package.json').write_text(json.dumps(package, indent=2) + '\n')
    for name in ['LICENSE', 'THIRD_PARTY_NOTICES.md']:
        if (source_root / name).is_file():
            shutil.copyfile(source_root / name, runtime_root / name)
    verify_tree(runtime_root)
    print(json.dumps({'status': 'built', 'version': VERSION, 'entrypoint': 'bin/rea.mjs'}))


def verify_tree(runtime_root):
    required = {'bin/rea.mjs', 'lib/javascript_worker.mjs', 'package.json'}
    allowed = required | {'LICENSE', 'THIRD_PARTY_NOTICES.md', '.rea_runtime.json'}
    files = set()
    for path in runtime_root.rglob('*'):
        if path.is_symlink():
            raise RuntimeError('Linked runtime file: ' + str(path))
        if path.is_file():
            files.add(path.relative_to(runtime_root).as_posix())
    if not required <= files or not files <= allowed:
        raise RuntimeError('Unexpected runtime file tree: ' + repr(sorted(files)))
    for name in ['bin/rea.mjs', 'lib/javascript_worker.mjs']:
        text = (runtime_root / name).read_text()
        # Module imports, not strings describing APIs found in target source.
        if re.search(r'(?:from|import)\s*[\"\']node:(?:net|http|https|tls|dgram)[\"\']', text):
            raise RuntimeError('Network module in local runtime: ' + name)
        for marker in ['--incur-update-check', '--incur-binary-apply', 'metrics.publish',
                       'diagnostics_channel', 'durationMs', 'registry.npmjs.org',
                       'createServer(', '.listen(']:
            if marker in text:
                raise RuntimeError('Excluded implementation in local runtime: ' + marker)


def invoke(runtime_root, arguments, environment, *, success=True):
    result = subprocess.run(['node', str(runtime_root / 'bin/rea.mjs'), *arguments],
                            env=environment, text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, timeout=360)
    if (result.returncode == 0) != success:
        raise RuntimeError('Unexpected command status: ' + repr(arguments) + '\n'
                           + result.stderr[-3000:] + '\n' + result.stdout[-3000:])
    return result


def make_asar(path, text):
    payload = text.encode()
    header = json.dumps({'files': {'index.js': {'size': len(payload), 'offset': '0'}}},
                        separators=(',', ':')).encode()
    string_payload = struct.pack('<I', len(header)) + header
    string_payload += b'\0' * ((-len(string_payload)) % 4)
    pickle = struct.pack('<I', len(string_payload)) + string_payload
    path.write_bytes(struct.pack('<II', 4, len(pickle)) + pickle + payload)


def verify(runtime_root):
    check_node()
    runtime_root = runtime_root.resolve()
    verify_tree(runtime_root)
    with tempfile.TemporaryDirectory(prefix='rea_local_verify_') as directory:
        root = Path(directory)
        environment = os.environ.copy()
        environment['TMPDIR'] = str(root / 'temporary')
        (root / 'temporary').mkdir()
        result = invoke(runtime_root, ['--version'], environment)
        if result.stdout.strip() != VERSION:
            raise RuntimeError('Wrong local runtime version')
        app = root / 'app'
        app.mkdir()
        (app / 'package.json').write_text('{"name":"fixture","version":"1.0.0","main":"index.js"}\n')
        marker = root / 'target_was_executed'
        code = ('const fs = require("node:fs");\n'
                + 'fs.writeFileSync(' + json.dumps(str(marker)) + ', "executed");\n'
                + 'exports.square = function square(value) { return value * value; };\n')
        (app / 'index.js').write_text(code)
        before = hashlib.sha256((app / 'index.js').read_bytes()).hexdigest()
        result = invoke(runtime_root, ['analyze-javascript-application', str(app), '--json'], environment)
        evidence = json.loads(result.stdout)
        if evidence.get('operation') != 'analyze_javascript_application' or marker.exists():
            raise RuntimeError('Static analysis did not return valid inert-source Evidence')
        if before != hashlib.sha256((app / 'index.js').read_bytes()).hexdigest():
            raise RuntimeError('Source input changed during static analysis')
        page = None
        for view in [{'kind': 'summary'}, {'kind': 'page', 'collection': 'modules', 'offset': 0, 'limit': 4}]:
            request = root / 'view.json'
            request.write_text(json.dumps({'source': {'kind': 'inline', 'evidence': evidence}, 'view': view}))
            result = invoke(runtime_root, ['inspect-analysis-view', str(request), '--json'], environment)
            value = json.loads(result.stdout)
            if value.get('operation') != 'inspect_analysis_view':
                raise RuntimeError('Saved Evidence view failed')
            if view['kind'] == 'page':
                page = value['normalized_result']['items']
        if not page:
            raise RuntimeError('No module identities returned by the saved Evidence page')
        request.write_text(json.dumps({'source': {'kind': 'inline', 'evidence': evidence},
                                      'view': {'kind': 'item', 'collection': 'modules',
                                               'selector': {'node_id': page[0]['node_id']}}}))
        result = invoke(runtime_root, ['inspect-analysis-view', str(request), '--json'], environment)
        if json.loads(result.stdout).get('operation') != 'inspect_analysis_view':
            raise RuntimeError('Saved module item view failed')
        damaged = dict(evidence)
        damaged['evidence_id'] = 'ev_' + '0' * 64
        request.write_text(json.dumps({'source': {'kind': 'inline', 'evidence': damaged},
                                      'view': {'kind': 'summary'}}))
        invoke(runtime_root, ['inspect-analysis-view', str(request), '--json'], environment, success=False)
        archive = root / 'fixture.asar'
        make_asar(archive, 'exports.answer = function answer() { return 42; };\n')
        result = invoke(runtime_root, ['analyze-javascript-application', str(archive), '--json'], environment)
        if json.loads(result.stdout).get('operation') != 'analyze_javascript_application':
            raise RuntimeError('Static ASAR analysis failed')
        for command in ['setup', 'mcp', 'update', '--incur-update-check']:
            result = invoke(runtime_root, [command, str(app), '--json'], environment, success=False)
            if 'error' not in json.loads(result.stdout):
                raise RuntimeError('Unsupported command was not rejected')
        result = invoke(runtime_root, ['analyze-javascript-application', str(root / 'missing'), '--json'],
                        environment, success=False)
        if 'error' not in json.loads(result.stdout):
            raise RuntimeError('Missing input did not return a structured failure')
        archive.write_bytes(b'invalid asar')
        invoke(runtime_root, ['analyze-javascript-application', str(archive), '--json'], environment, success=False)
    print(json.dumps({'status': 'verified', 'version': VERSION,
                      'checks': ['inert_directory', 'asar', 'summary', 'module_page', 'module_item',
                                 'evidence_integrity', 'input_unchanged', 'excluded_commands',
                                 'structured_failures', 'runtime_tree']}))


def main():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest='command', required=True)
    builder = commands.add_parser('build')
    builder.add_argument('--source-root', type=Path, required=True)
    builder.add_argument('--runtime-root', type=Path, required=True)
    builder.add_argument('--offline', action='store_true')
    verifier = commands.add_parser('verify')
    verifier.add_argument('--runtime-root', type=Path, required=True)
    args = parser.parse_args()
    if args.command == 'build':
        build(args.source_root, args.runtime_root, args.offline)
    else:
        verify(args.runtime_root)


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
