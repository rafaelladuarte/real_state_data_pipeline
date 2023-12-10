CREATE TABLE olist.star_schema.payments (
	payment_id UUID PRIMARY KEY,
	payment_order_id UUID,
	payment_type VARCHAR(20),
	payment_count INT,
	payment_parcel INT,
	payment_vl DOUBLE PRECISION
);