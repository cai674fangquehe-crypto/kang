import subprocess
import sys

print("Python entrypoint started.")

try:
    # Run the bash script
    result = subprocess.run(['./setup.sh'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Bash script output:")
    print(result.stdout)
    print("Bash script finished successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error running bash script: {e.stderr}")
    sys.exit(1)

print("Continuing with Python application logic...")
# Add main application logic here
