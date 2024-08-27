import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# Ensure the .kaggle directory exists
os.makedirs(os.path.expanduser('~/.kaggle'), exist_ok=True)

# Move the kaggle.json file to the .kaggle directory
kaggle_json_path = 'C:/Users/matth/Downloads/kaggle.json'
kaggle_destination_path = os.path.expanduser('~/.kaggle/kaggle.json')
if not os.path.exists(kaggle_destination_path):
    os.rename(kaggle_json_path, kaggle_destination_path)

# Set permissions for the kaggle.json file
os.chmod(kaggle_destination_path, 0o600)

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Define the path to download and extract the dataset
download_path = 'C:/Users/matth/ecommerce_mba_project/data/raw/unlock-profits-with-e-commerce-sales-data.zip'
extract_dir = 'C:/Users/matth/ecommerce_mba_project/data/raw'

# Download the dataset
api.dataset_download_files('thedevastator/unlock-profits-with-e-commerce-sales-data', path='C:/Users/matth/ecommerce_mba_project/data/raw', unzip=False)

# Extract the ZIP file
with zipfile.ZipFile(download_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

print("Download and extraction complete.")
