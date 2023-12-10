INSERT INTO olist.star_schema.items
SELECT 
	uuid_generate_v4()::UUID AS item_id,
	order_id::UUID AS item_order_id,
	product_id::UUID AS item_product_id,
	shipping_limit_date::TIMESTAMP AS item_ship_limit_dt,
	price AS item_price_vl,
	freight_value AS item_freight_vl 
FROM olist.raw.olist_order_items_dataset