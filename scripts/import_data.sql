-- Import data into amazon_orders table
\copy amazon_orders(order_id, date, status, fulfillment, sales_channel, ship_service_level, courier_status, currency, amount, ship_city, ship_state, ship_postal_code, ship_country, promotion_ids, b2b, fulfilled_by) FROM 'C:/Users/matth/ecommerce_mba_project/data/cleaned/amazon_orders_cleaned.csv' DELIMITER ',' CSV HEADER;

-- Import data into amazon_products table
\copy amazon_products(sku, style, category, size, asin, product_name) FROM 'C:/Users/matth/ecommerce_mba_project/data/cleaned/amazon_products_with_names.csv' DELIMITER ',' CSV HEADER;

-- Import data into amazon_order_items table
\copy amazon_order_items(order_id, sku, style, category, size, asin, qty, amount) FROM 'C:/Users/matth/ecommerce_mba_project/data/cleaned/amazon_order_items_cleaned.csv' DELIMITER ',' CSV HEADER;

-- Import data into sale_report table
\copy sale_report(sku_code, design_no, stock, category, size, color) FROM 'C:/Users/matth/ecommerce_mba_project/data/cleaned/sale_report_cleaned.csv' DELIMITER ',' CSV HEADER;

-- Import data into p_and_l_march_2021 table
\copy p_and_l_march_2021(sku, style_id, catalog, category, weight, tp1, tp2, mrp_old, final_mrp_old, ajio_mrp, amazon_mrp, amazon_fba_mrp, flipkart_mrp, limeroad_mrp, myntra_mrp, paytm_mrp, snapdeal_mrp) FROM 'C:/Users/matth/ecommerce_mba_project/data/cleaned/p_and_l_march_2021_cleaned.csv' DELIMITER ',' CSV HEADER;

-- Import data into may_2022 table
\copy may_2022(sku, style_id, catalog, category, weight, tp, mrp_old, final_mrp_old, ajio_mrp, amazon_mrp, amazon_fba_mrp, flipkart_mrp, limeroad_mrp, myntra_mrp, paytm_mrp, snapdeal_mrp) FROM 'C:/Users/matth/ecommerce_mba_project/data/cleaned/may_2022_cleaned.csv' DELIMITER ',' CSV HEADER;
