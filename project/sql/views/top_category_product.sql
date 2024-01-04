CREATE OR REPLACE VIEW top_category_product 
AS SELECT
	B.category_name, 
	COUNT(*) AS count_product
FROM star_schema.products A
INNER JOIN star_schema.category B ON A.product_category_id = B.category_id
GROUP BY 1
ORDER BY 2 DESC;