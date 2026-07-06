"""Example: CLI Usage.

This example demonstrates how to use the SocialMedia-Hub CLI.
"""

import subprocess
import sys


def run_command(cmd: str) -> str:
    """Run a shell command and return output."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"


def main():
    """Main function."""
    print("=== SocialMedia-Hub CLI Examples ===\n")

    # 1. Check version
    print("1. Check version:")
    output = run_command("smh version")
    print(f"   {output.strip()}\n")

    # 2. Health check
    print("2. Health check:")
    output = run_command("smh health")
    print(f"   {output.strip()}\n")

    # 3. Start server
    print("3. Start server (run in background):")
    print("   smh-server start --port 8000\n")

    # 4. Create API key
    print("4. Create API key:")
    print("   smh create-key --name myapp --tier pro\n")

    # 5. Fetch URL
    print("5. Fetch social media URL:")
    print('   smh fetch "https://v.douyin.com/abc/"\n')

    # 6. Server status
    print("6. Check server status:")
    print("   smh-server status\n")

    print("=== End of Examples ===")


if __name__ == "__main__":
    main()
