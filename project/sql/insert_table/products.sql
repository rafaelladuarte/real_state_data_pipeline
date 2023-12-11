INSERT INTO olist.star_schema.products
	SELECT 
		product_id::UUID,
		category_id::UUID,
		product_name_lenght::INT,
		product_description_lenght::INT AS product_describe_lenght,
		product_photos_qty::INT,
		product_weight_g::INT,
		product_length_cm::INT,
		product_height_cm::INT,
		product_width_cm::INT
	FROM olist.raw.olist_products_dataset AS A
	INNER JOIN star_schema.category AS B ON
		INITCAP(REPLACE(A.product_category_name, '_', ' ')) = B.category_name;