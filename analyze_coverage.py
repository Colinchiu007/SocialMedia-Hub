import subprocess
import re

result = subprocess.run(
    ['python', '-m', 'pytest', 'tests/', '--cov=socialmedia_hub', '--cov-report=term', '-q'],
    capture_output=True, text=True, cwd='D:\\Data\\MimoCode\\SocialMedia-Hub'
)

output = result.stdout + result.stderr

# Parse coverage output
lines = re.findall(r'(\S+\.py)\s+(\d+)\s+(\d+)\s+(\d+)%', output)

# Sort by uncovered lines (column 3)
lines.sort(key=lambda x: -int(x[2]))

print('Top 20 files by uncovered lines:')
for name, total, uncovered, pct in lines[:20]:
    print(f'{name}: {uncovered}/{total} uncovered ({pct}%)')

print(f'\nTotal lines: {sum(int(x[1]) for x in lines)}')
print(f'Total uncovered: {sum(int(x[2]) for x in lines)}')
print(f'Coverage: {(1 - sum(int(x[2]) for x in lines) / sum(int(x[1]) for x in lines)) * 100:.1f}%')
