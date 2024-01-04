CREATE OR REPLACE VIEW count_order_status
AS SELECT 
	order_status,
	COUNT ( DISTINCT product_id) AS count_order_status
FROM star_schema.orders 
GROUP BY 1
ORDER BY 2 DESC