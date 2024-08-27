import zipfile
import os

# Define the path to the ZIP file and extraction directory
zip_path = 'C:/Users/matth/unlock-profits-with-e-commerce-sales-data.zip'
extract_dir = 'C:/Users/matth/ecommerce_mba_project/data/raw'

# Ensure the extraction directory exists
if not os.path.exists(extract_dir):
    os.makedirs(extract_dir)

# Extract the ZIP file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

print("Extraction complete.")
