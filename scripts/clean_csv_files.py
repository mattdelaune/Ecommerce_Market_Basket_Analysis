import pandas as pd
import os

# Define the base path to the CSV files
base_path = 'C:/Users/matth/ecommerce_mba_project/data/raw'
cleaned_path = 'C:/Users/matth/ecommerce_mba_project/data/cleaned'
log_path = 'C:/Users/matth/ecommerce_mba_project/data/logs'

# Ensure the cleaned path and log path exist
os.makedirs(cleaned_path, exist_ok=True)
os.makedirs(log_path, exist_ok=True)

# Define the paths to the CSV files using os.path.join
csv_files = {
    'sale_report': os.path.join(base_path, 'Sale Report.csv'),
    'p_and_l_march_2021': os.path.join(base_path, 'P  L March 2021.csv'),
    'amazon_sale_report': os.path.join(base_path, 'Amazon Sale Report.csv'),
    'may_2022': os.path.join(base_path, 'May-2022.csv')
}

# Define the columns to keep and their new formatted names
columns_to_keep = {
    'sale_report': ['SKU Code', 'Design No.', 'Stock', 'Category', 'Size', 'Color'],
    'p_and_l_march_2021': ['Sku', 'Style Id', 'Catalog', 'Category', 'Weight', 'TP 1', 'TP 2', 'MRP Old', 'Final MRP Old', 'Ajio MRP', 'Amazon MRP', 'Amazon FBA MRP', 'Flipkart MRP', 'Limeroad MRP', 'Myntra MRP', 'Paytm MRP', 'Snapdeal MRP'],
    'amazon_sale_report': ['Order ID', 'Date', 'Status', 'Fulfilment', 'Sales Channel ', 'ship-service-level', 'Style', 'SKU', 'Category', 'Size', 'ASIN', 'Courier Status', 'Qty', 'currency', 'Amount', 'B2B', 'fulfilled-by'],
    'may_2022': ['Sku', 'Style Id', 'Catalog', 'Category', 'Weight', 'TP', 'MRP Old', 'Final MRP Old', 'Ajio MRP', 'Amazon MRP', 'Amazon FBA MRP', 'Flipkart MRP', 'Limeroad MRP', 'Myntra MRP', 'Paytm MRP', 'Snapdeal MRP']
}

# Define the new column names
formatted_columns = {
    'sale_report': ['sku_code', 'design_no', 'stock', 'category', 'size', 'color'],
    'p_and_l_march_2021': ['sku', 'style_id', 'catalog', 'category', 'weight', 'tp1', 'tp2', 'mrp_old', 'final_mrp_old', 'ajio_mrp', 'amazon_mrp', 'amazon_fba_mrp', 'flipkart_mrp', 'limeroad_mrp', 'myntra_mrp', 'paytm_mrp', 'snapdeal_mrp'],
    'amazon_sale_report': ['order_id', 'date', 'status', 'fulfilment', 'sales_channel', 'ship_service_level', 'style', 'sku', 'category', 'size', 'asin', 'courier_status', 'qty', 'currency', 'amount', 'b2b', 'fulfilled_by'],
    'may_2022': ['sku', 'style_id', 'catalog', 'category', 'weight', 'tp', 'mrp_old', 'final_mrp_old', 'ajio_mrp', 'amazon_mrp', 'amazon_fba_mrp', 'flipkart_mrp', 'limeroad_mrp', 'myntra_mrp', 'paytm_mrp', 'snapdeal_mrp']
}

# Define data type corrections
data_type_corrections = {
    'stock': 'float',
    'weight': 'float',
    'tp1': 'float',
    'tp2': 'float',
    'mrp_old': 'float',
    'final_mrp_old': 'float'
}

# Clean the CSV files
for key, path in csv_files.items():
    if os.path.exists(path):
        df = pd.read_csv(path, low_memory=False)
        print(f"Columns in {path}: {df.columns.tolist()}")
        
        # Replace 'Nill', '#VALUE!', and other invalid entries with None
        df.replace(['Nill', 'nil', 'None', '', '#VALUE!'], None, inplace=True)
        
        # Convert columns to appropriate data types
        for col, dtype in data_type_corrections.items():
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Log problematic rows
        problematic_rows = df[df.isnull().any(axis=1)]
        if not problematic_rows.empty:
            log_file = os.path.join(log_path, f'{key}_log.csv')
            problematic_rows.to_csv(log_file, index=False)
            print(f"Logged problematic rows to {log_file}")

        # Keep only the required columns and rename them
        try:
            df = df[columns_to_keep[key]]
        except KeyError as e:
            print(f"Error processing {path}: {e}")
            continue
        df.columns = formatted_columns[key]
        
        # Handle missing values appropriately
        df.fillna({'stock': 0, 'weight': 0, 'tp1': 0, 'tp2': 0, 'mrp_old': 0, 'final_mrp_old': 0}, inplace=True)
        
        # Write the cleaned data back to a new CSV file
        new_path = os.path.join(cleaned_path, key + '_cleaned.csv')
        df.to_csv(new_path, index=False)
        print(f"Saved cleaned data to {new_path}")
    else:
        print(f"File not found: {path}")

print("CSV files cleaned and saved.")
