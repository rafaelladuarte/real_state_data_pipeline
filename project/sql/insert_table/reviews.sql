INSERT INTO olist.star_schema.reviews
	SELECT 
		uuid_generate_v4()::UUID review_id,
		order_id::UUID AS review_order_id,
		review_score::INT,
		review_comment_title::VARCHAR(100) review_title ,
		review_comment_message::TEXT AS review_message,
		review_creation_date::TIMESTAMP AS review_create_dt,
		review_answer_timestamp::TIMESTAMP AS review_answer_dt 
	FROM olist.raw.olist_order_reviews_dataset