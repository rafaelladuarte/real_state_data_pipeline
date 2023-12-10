CREATE TABLE olist.star_schema.payment (
	payment_id UUID PRIMARY KEY,
	payment_type VARCHAR(20),
	payment_seq INT,
	payment_parcel INT,
	payment_vl DOUBLE PRECISION
);