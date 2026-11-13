import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));
const cli = fileURLToPath(new URL('../node_modules/@fission-ai/openspec/bin/openspec.js', import.meta.url));
for (const extra of [[], ['--archived']]) {
  const result = spawnSync(process.execPath, [cli, 'validate', '--all', '--strict', '--no-interactive', ...extra], {
    cwd: root,
    env: { ...process.env, OPENSPEC_TELEMETRY: '0' },
    stdio: 'inherit',
  });
  if (result.error) console.error(result.error.message);
  if (result.status !== 0) process.exit(result.status ?? 1);
}
