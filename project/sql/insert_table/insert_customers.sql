WITH MeanGeolocations AS (
    SELECT
        B.zip_code_prefix,
        AVG(B.latitude) AS latitude_mean,
        AVG(B.longitude) AS longitude_mean
    FROM
        olist.raw.olist_customers_dataset AS A
    JOIN
        star_schema.geolocation AS B ON A.customer_zip_code_prefix = B.zip_code_prefix
    GROUP BY
        B.zip_code_prefix
)

INSERT INTO star_schema.customers
SELECT DISTINCT ON (A.customer_id)
    A.customer_id::UUID,
	B.geolocation_id AS customer_geolocation_id
FROM
    olist.raw.olist_customers_dataset AS A
JOIN
    star_schema.geolocation AS B ON A.customer_zip_code_prefix = B.zip_code_prefix
JOIN
    MeanGeolocations AS MG ON A.customer_zip_code_prefix = MG.zip_code_prefix
ORDER BY
    A.customer_id,
    point(MG.longitude_mean, MG.latitude_mean) <-> point(B.longitude, B.latitude)
