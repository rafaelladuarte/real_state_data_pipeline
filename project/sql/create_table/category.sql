CREATE TABLE IF NOT EXISTS olist.star_schema.category (
	category_id UUID PRIMARY KEY,
	category_name VARCHAR(50),
	category_tree TEXT
);
