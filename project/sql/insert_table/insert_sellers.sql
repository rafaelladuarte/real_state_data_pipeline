WITH MeanGeolocations AS (
    SELECT
        B.zip_code_prefix,
        AVG(B.latitude) AS latitude_mean,
        AVG(B.longitude) AS longitude_mean
    FROM
        olist.raw.olist_sellers_dataset AS A
    JOIN
        star_schema.geolocation AS B ON A.seller_zip_code_prefix = B.zip_code_prefix
    GROUP BY
        B.zip_code_prefix
)

INSERT INTO star_schema.sellers
SELECT DISTINCT ON (A.seller_id)
    A.seller_id::UUID,
	B.geolocation_id AS seller_geolocation_id
FROM
    olist.raw.olist_sellers_dataset AS A
JOIN
    star_schema.geolocation AS B ON A.seller_zip_code_prefix = B.zip_code_prefix
JOIN
    MeanGeolocations AS MG ON A.seller_zip_code_prefix = MG.zip_code_prefix
ORDER BY
    A.seller_id,
    point(
		MG.longitude_mean, MG.latitude_mean) <-> point(B.longitude,B.latitude)
