INSERT INTO olist.star_schema.category
SELECT 
	uuid_generate_v4()::uuid AS category_id,
	INITCAP(REPLACE(product_category_name, '_', ' ')) AS category_name
FROM olist_raw.product_category_name_translation;