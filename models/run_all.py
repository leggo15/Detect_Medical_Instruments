import subprocess
import os
import shutil

# Verify that 'jupyter' is installed
if shutil.which("jupyter") is None:
    print("Error: 'jupyter' is not installed or not found in PATH.")
    exit(1)

# List of notebook filenames to run
notebooks = [
    "base_model.ipynb",
    "augmentation_models/augmentation-crop-model.ipynb",
    "augmentation_models/augmentation-flip-model.ipynb",
    "augmentation_models/augmentation-rotate-model.ipynb",
    "augmentation_models/augmentation-rotate-and-base-model.ipynb",
    "augmentation_models/augmentation-all-model.ipynb",
    "resolution_models/image_resolution_model-64.ipynb",
    "resolution_models/image_resolution_model-256.ipynb",
    "resolution_models/image_resolution_model-720.ipynb",
    "resolution_models/image_resolution_model-1024.ipynb",
    "data_size_test/data_size_25.ipynb",
    "data_size_test/data_size_50.ipynb",
    "data_size_test/data_size_75.ipynb",
]

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

for nb in notebooks:
    # Construct the full path relative to the current script directory
    notebook_full_path = os.path.join(current_dir, nb)
    
    if not os.path.isfile(notebook_full_path):
        print(f"Notebook not found: {notebook_full_path}. Skipping...")
        continue  # Skip to the next notebook

    print(f"Running {notebook_full_path}...")

    try:
        subprocess.run(
            ["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", notebook_full_path],
            check=True
        )
        print(f"Successfully executed {notebook_full_path}.")
    except subprocess.CalledProcessError:
        print(f"Error executing {notebook_full_path}.")