CREATE TABLE olist.star_schema.item (
	item_id UUID PRIMARY KEY,
	item_limit_qty TIMESTAMP,
	item_price_vl DOUBLE PRECISION,
	item_freight_vl DOUBLE PRECISION
);
