SELECT  
	geolocation_zip_code_prefix as zip_code_prefix,
	geolocation_lat as latitude,
	geolocation_lng as longitude,
	INITCAP(geolocation_city) as cidade,
	geolocation_state as uf
FROM olist_raw.olist_geolocation_dataset;

SELECT 
	seller_id AS vendedor_id,
	'nome teste' AS vendedor_nome,
	seller_zip_code_prefix AS vendedor_zip_code_prefix
FROM olist_raw.olist_sellers_dataset;

SELECT 
	customer_id AS cliente_id,
	'nome teste' AS cliente_nome,
	customer_zip_code_prefix AS cliente_zip_code_prefix
FROM olist_raw.olist_customers_dataset;

SELECT 
	uuid_generate_v4()::uuid AS categoria_id,
	INITCAP(REPLACE(product_category_name, '_', ' ')) AS categoria_nome
FROM olist_raw.product_category_name_translation;