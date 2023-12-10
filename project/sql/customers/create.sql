CREATE TABLE olist.star_schema.customers (
	customer_id UUID PRIMARY KEY,
	customer_name VARCHAR(100),
	customer_geolocation_id UUID,
	FOREIGN KEY (customer_geolocation_id) REFERENCES olist.star_schema.geolocation (geolocation_id)
);