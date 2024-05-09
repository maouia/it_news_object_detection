import subprocess
import sys


def install_dependencies():
    try:
        with open('requirements', 'r') as f:
            requirements = f.readlines()
            requirements = [req.strip() for req in requirements if req.strip()]

        if requirements:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements'])
            print("All dependencies have been successfully installed.")
        else:
            print("No dependencies found in requirements.txt.")

    except FileNotFoundError:
        print("requirements.txt file not found.")

if __name__ == "__main__":
    install_dependencies()
