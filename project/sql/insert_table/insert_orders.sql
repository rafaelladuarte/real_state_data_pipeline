INSERT INTO olist.star_schema.orders
SELECT 
    uuid_generate_v4()::UUID AS order_unique_id,
    A.order_id::UUID,
    A.customer_id::UUID,
    B.seller_id::UUID,
    B.product_id::UUID, 
    D.category_id::UUID,
    E.review_id::UUID,
    F.item_id::UUID,
    G.payment_id::UUID,
    order_status::VARCHAR(50),
    order_purchase_timestamp::TIMESTAMP AS order_dt,
    order_approved_at::TIMESTAMP AS order_approved_dt,
    order_delivered_carrier_date::TIMESTAMP AS order_sent_dt,
    order_delivered_customer_date::TIMESTAMP AS order_received_dt,
    order_estimated_delivery_date::TIMESTAMP AS order_delivery_forecast_dt 
FROM 
    olist.raw.olist_orders_dataset A
    JOIN olist.raw.olist_order_items_dataset B ON A.order_id = B.order_id
    JOIN olist.raw.olist_products_dataset C ON B.product_id = C.product_id
    LEFT JOIN star_schema.category D ON INITCAP(REPLACE(C.product_category_name, '_', ' ')) = D.category_name
    LEFT JOIN star_schema.reviews E ON A.order_id::UUID = E.review_order_id
    LEFT JOIN star_schema.items F ON A.order_id::UUID = F.item_order_id
    LEFT JOIN star_schema.payment G ON A.order_id::UUID = G.payment_order_id
WHERE 
    B.seller_id::UUID IN (SELECT seller_id FROM star_schema.sellers)
    AND A.customer_id::UUID IN (SELECT customer_id FROM star_schema.customers)
    AND B.product_id::UUID IN (SELECT product_id FROM star_schema.product);

