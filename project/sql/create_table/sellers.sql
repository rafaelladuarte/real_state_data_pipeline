CREATE TABLE IF NOT EXISTS olist.star_schema.sellers (
	seller_id UUID PRIMARY KEY ,
	seller_name VARCHAR(100),
	seller_geolocation_id UUID,
	FOREIGN KEY (seller_geolocation_id) REFERENCES olist.star_schema.geolocation (geolocation_id)
);