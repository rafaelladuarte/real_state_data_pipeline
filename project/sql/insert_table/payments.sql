INSERT INTO olist.star_schema.payments
	SELECT
		uuid_generate_v4()::UUID as payment_id,
		order_id::UUID AS payment_order_id,
		payment_type,
		payment_sequential AS payment_count,
		payment_installments AS payment_parcel,
		payment_value payment_vl
	FROM 
		olist.raw.olist_order_payments_dataset