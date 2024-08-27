-- Create amazon_orders table
CREATE TABLE amazon_orders (
    order_id VARCHAR(50) PRIMARY KEY,
    date DATE,
    status VARCHAR(255),
    fulfillment VARCHAR(255),
    sales_channel VARCHAR(255),
    ship_service_level VARCHAR(255),
    courier_status VARCHAR(255),
    currency VARCHAR(50),
    amount REAL,
    ship_city VARCHAR(255),
    ship_state VARCHAR(255),
    ship_postal_code VARCHAR(50),
    ship_country VARCHAR(50),
    promotion_ids TEXT,
    b2b BOOLEAN,
    fulfilled_by VARCHAR(255)
);

-- Create amazon_products table
CREATE TABLE amazon_products (
    sku VARCHAR(50) PRIMARY KEY,
    style VARCHAR(255),
    category VARCHAR(255),
    size VARCHAR(50),
    asin VARCHAR(50),
    product_name VARCHAR(255),
    CHECK (sku IS NOT NULL AND sku <> '')
);

-- Create amazon_order_items table
CREATE TABLE amazon_order_items (
    order_id VARCHAR(50),
    sku VARCHAR(50),
    style VARCHAR(255),
    category VARCHAR(255),
    size VARCHAR(50),
    asin VARCHAR(50),
    qty INTEGER,
    amount REAL,
    PRIMARY KEY (order_id, sku),
    FOREIGN KEY (order_id) REFERENCES amazon_orders(order_id),
    FOREIGN KEY (sku) REFERENCES amazon_products(sku)
);

-- Create sale_report table
CREATE TABLE sale_report (
    id SERIAL PRIMARY KEY,
    sku_code VARCHAR(50),
    design_no VARCHAR(50),
    stock REAL,
    category VARCHAR(255),
    size VARCHAR(50),
    color VARCHAR(50),
    FOREIGN KEY (sku_code) REFERENCES amazon_products(sku)
);

-- Create p_and_l_march_2021 table
CREATE TABLE p_and_l_march_2021 (
    id SERIAL PRIMARY KEY,
    sku VARCHAR(50),
    style_id VARCHAR(50),
    catalog VARCHAR(255),
    category VARCHAR(255),
    weight REAL,
    tp1 REAL,
    tp2 REAL,
    mrp_old REAL,
    final_mrp_old REAL,
    ajio_mrp REAL,
    amazon_mrp REAL,
    amazon_fba_mrp REAL,
    flipkart_mrp REAL,
    limeroad_mrp REAL,
    myntra_mrp REAL,
    paytm_mrp REAL,
    snapdeal_mrp REAL,
    FOREIGN KEY (sku) REFERENCES amazon_products(sku)
);

-- Create may_2022 table
CREATE TABLE may_2022 (
    id SERIAL PRIMARY KEY,
    sku VARCHAR(50),
    style_id VARCHAR(50),
    catalog VARCHAR(255),
    category VARCHAR(255),
    weight REAL,
    tp REAL,
    mrp_old REAL,
    final_mrp_old REAL,
    ajio_mrp REAL,
    amazon_mrp REAL,
    amazon_fba_mrp REAL,
    flipkart_mrp REAL,
    limeroad_mrp REAL,
    myntra_mrp REAL,
    paytm_mrp REAL,
    snapdeal_mrp REAL,
    FOREIGN KEY (sku) REFERENCES amazon_products(sku)
);
