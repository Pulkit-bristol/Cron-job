import os
import subprocess
from datetime import datetime

# Configuration
REPO_PATH = os.getenv("REPO_PATH", ".")  # GitHub Actions sets this automatically
FILE_TO_UPDATE = "daily_update_log.txt"
COMMIT_MESSAGE = "Daily update: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def update_file(file_path):
    """Update the file with a timestamp."""
    with open(file_path, 'a') as f:
        f.write(f"Updated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def run_git_commands():
    """Run git commands to add, commit, and push changes."""
    try:
        subprocess.run(["git", "add", FILE_TO_UPDATE], check=True, cwd=REPO_PATH)
        subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], check=True, cwd=REPO_PATH)
        subprocess.run(["git", "push"], check=True, cwd=REPO_PATH)
        print("Changes pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Git command: {e}")

if __name__ == "__main__":
    file_path = os.path.join(REPO_PATH, FILE_TO_UPDATE)

    # Ensure the file exists
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write("Daily updates:\n")

    update_file(file_path)
    run_git_commands()
