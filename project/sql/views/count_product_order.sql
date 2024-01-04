CREATE OR REPLACE VIEW count_product_order
AS SELECT 
	order_id,
	COUNT (product_id) AS count_product
FROM star_schema.orders
GROUP BY 1
ORDER BY 2 DESC