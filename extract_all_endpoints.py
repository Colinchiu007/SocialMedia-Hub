"""Extract actual endpoints from auto-generated route files."""
import re
import os

def extract_endpoints(filepath):
    with open(filepath) as f:
        content = f.read()

    # Find all GET/POST endpoints with their parameters
    pattern = r'@router\.(get|post)\("(/[^"]+)"\)\nasync def \w+\((.*?)\)'
    matches = re.findall(pattern, content, re.DOTALL)

    endpoints = []
    for method, path, params_block in matches:
        # Extract parameter names (excluding request, token)
        params = re.findall(r'(\w+):\s*(?:str|int|float|bool)', params_block)
        if not params:
            params = re.findall(r'(\w+):\s*(?:str|int|float|bool)\s*\|', params_block)
        endpoints.append((method, path, params))

    return endpoints

# Process each auto route file
routes_dir = 'src/socialmedia_hub/server/routes'
results = {}

for filename in sorted(os.listdir(routes_dir)):
    if filename.startswith('auto_') and filename.endswith('.py'):
        filepath = os.path.join(routes_dir, filename)
        endpoints = extract_endpoints(filepath)
        if endpoints:
            results[filename] = endpoints

# Print summary
for filename, endpoints in sorted(results.items()):
    print(f"\n{filename}: {len(endpoints)} endpoints")
    for method, path, params in endpoints[:5]:
        print(f"  {method.upper()} {path}: {params}")
    if len(endpoints) > 5:
        print(f"  ... and {len(endpoints) - 5} more")
