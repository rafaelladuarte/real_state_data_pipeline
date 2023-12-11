INSERT INTO olist.star_schema.geolocation
	SELECT  
		uuid_generate_v4()::uuid AS geolocation_id,
		geolocation_zip_code_prefix AS zip_code_prefix,
		geolocation_lat AS latitude,
		geolocation_lng AS longitude,
		INITCAP(geolocation_city) AS city,
		geolocation_state AS uf
	FROM olist.raw.olist_geolocation_dataset;