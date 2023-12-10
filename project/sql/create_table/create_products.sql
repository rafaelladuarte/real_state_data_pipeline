CREATE TABLE olist.star_schema.product (
	product_id UUID PRIMARY KEY,
	product_category_id UUID,
	product_name_tm INT,
	product_describe_tm INT,
	product_photos_qty INT,
	product_weight_g INT,
	product_length_cm INT,
	product_height_cm INT,
	product_width_cm INT,
	FOREIGN KEY (product_category_id) REFERENCES olist.star_schema.category (category_id)
);
