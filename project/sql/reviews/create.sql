CREATE TABLE olist.star_schema.reviews (
	review_id UUID PRIMARY KEY,
	review_score INT,
	review_title VARCHAR(100),
	review_message TEXT,
	review_create_dt TIMESTAMP,
	review_answer_dt TIMESTAMP
);