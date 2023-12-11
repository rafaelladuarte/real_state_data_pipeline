CREATE TABLE IF NOT EXISTS olist.star_schema.items (
	item_id UUID PRIMARY KEY,
	item_order_id UUID,
	item_product_id UUID,
	item_ship_limit_dt TIMESTAMP,
	item_price_vl DOUBLE PRECISION,
	item_freight_vl DOUBLE PRECISION
);
