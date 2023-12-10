CREATE TABLE olist.star_schema.orders (
	order_id UUID PRIMARY KEY,
	customer_id UUID,
	seller_id UUID,
	product_id UUID, 
	category_id UUID,
	review_id_id UUID,
	item_id UUID,
	payment_id UUID,
	order_status VARCHAR(50),
	order_dt TIMESTAMP,
	order_approved_dt TIMESTAMP,
	order_sent_dt TIMESTAMP,
	order_delivery_forecast_dt TIMESTAMP,
	FOREIGN KEY (customer_id) REFERENCES olist.star_schema.customer (customer_id),
	FOREIGN KEY (seller_id) REFERENCES olist.star_schema.seller (seller_id),
	FOREIGN KEY (product_id) REFERENCES olist.star_schema.product (product_id),
	FOREIGN KEY (category_id) REFERENCES olist.star_schema.category (category_id),
	FOREIGN KEY (review_id_id) REFERENCES olist.star_schema.review_id (review_id_id),
	FOREIGN KEY (item_id) REFERENCES olist.star_schema.item (item_id),
	FOREIGN KEY (payment_id) REFERENCES olist.star_schema.payment (payment_id)
);