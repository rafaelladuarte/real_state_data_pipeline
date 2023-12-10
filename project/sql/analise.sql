-- VERIFICA  SE HÁ MÚLTIPLAS ENTRADAS PARA O UMA MESMA COLUNA MAS DIFERENTES PARA AS OUTRAS COLUNAS

-- Na tabela de geolocalização nao poderei utilizar a coluna 'geolocation_zip_code_prefix',
-- pois há múltiplas entradas. Dessa forma, terei de criar uma coluna nova para o ser o
-- identificador único do regitro da tabela.
SELECT
    geolocation_zip_code_prefix,
    COUNT(*) AS quantidade_de_entradas
FROM
    olist.raw.olist_geolocation_dataset
GROUP BY
    geolocation_zip_code_prefix
HAVING
    COUNT(*) > 1;

-- Na tabela de comentarios dos pedidos também não poderei utilizar a coluna 'review_id',
-- pois há múltiplas entradas. No entanto, nesse caso notei que dois campos juntos 
-- fornecem a unicidade desejada, sendo possivel atualizar a tabela criando uma 
-- chave primária composta por esses dois campos
SELECT
    review_id, order_id,
    COUNT(*) AS quantidade_de_entradas
FROM
    olist.raw.olist_order_reviews_dataset
GROUP BY
    review_id, order_id
HAVING
    COUNT(*) > 1;
	