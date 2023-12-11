CREATE TABLE IF NOT EXISTS olist.star_schema.geolocation (
	geolocation_id UUID PRIMARY KEY,
	zip_code_prefix INT,
	latitude DOUBLE PRECISION,
	longitude DOUBLE PRECISION,
	city VARCHAR(50),
	uf CHAR(2)
);