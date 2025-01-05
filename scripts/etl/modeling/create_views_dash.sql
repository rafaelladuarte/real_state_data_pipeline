CREATE OR REPLACE VIEW distribuicao_tipo AS
SELECT
    tipo,
    COUNT(*) AS quantidade
FROM public.imovel A
INNER JOIN public.tipo_imovel B ON A.id_tipo_imovel = B.id_tipo
GROUP BY tipo;

CREATE OR REPLACE VIEW distribuicao_modo AS
SELECT
	modo,
	COUNT(*) 
FROM public.imovel A
	INNER JOIN public.modo_imovel B ON A.id_modo_imovel = B.id_modo
GROUP BY  modo;

CREATE OR REPLACE VIEW distribuicao_bairro AS
SELECT 
	bairro,
	COUNT(*)
FROM public.endereco A
GROUP BY bairro

CREATE OR REPLACE  distribuicao_bairro_modo AS
SELECT 
	bairro,
	modo,
	COUNT(*)
FROM public.endereco A
INNER JOIN public.imovel B ON B.id_endereco_imovel = A.id_endereco
INNER JOIN public.modo_imovel C ON C.id_modo = B.id_modo_imovel
GROUP BY bairro, modo
ORDER BY bairro;

CREATE OR REPLACE VIEW media_preco_bairro_modo_tipo AS
SELECT 
	bairro,
	tipo,
	modo,
	ROUND(AVG(B.preco),2) AS media_preco
FROM public.endereco A
INNER JOIN public.imovel B ON B.id_endereco_imovel = A.id_endereco
INNER JOIN public.modo_imovel C ON C.id_modo = B.id_modo_imovel
INNER JOIN public.tipo_imovel D ON D.id_tipo = B.id_tipo_imovel
GROUP BY bairro, modo, tipo
ORDER BY bairro;

CREATE OR REPLACE VIEW media_preco_modo_tipo AS
SELECT 
	tipo,
	modo,
	ROUND(AVG(B.preco),2) AS media_preco
FROM public.imovel B
INNER JOIN public.modo_imovel C ON C.id_modo = B.id_modo_imovel
INNER JOIN public.tipo_imovel D ON D.id_tipo = B.id_tipo_imovel
GROUP BY modo, tipo
ORDER BY MODO;

CREATE OR REPLACE VIEW dispersao_preco_quartos_area AS
SELECT 
    id_imovel,
    preco,
    quantidade_quartos,
    area_m2
FROM 
    imovel
WHERE 
    preco IS NOT NULL
    AND (quantidade_quartos IS NOT NULL OR area_m2 IS NOT NULL)
	AND id_imovel != '1'
	AND id_imobiliaria != '1'
	AND id_endereco_imovel != '1'
	AND id_tipo_imovel != '1'
	AND id_modo_imovel != '1';

CREATE OR REPLACE VIEW dispersao_faixa_area_modo_tipo AS
SELECT 
    faixa_area,
	modo,
	tipo,
    COUNT(*)
FROM imovel A
INNER JOIN public.modo_imovel B
	ON A.id_modo_imovel = B.id_modo
INNER JOIN public.tipo_imovel C
	ON A.id_tipo_imovel = C.id_tipo
WHERE 
    preco IS NOT NULL
    AND (quantidade_quartos IS NOT NULL OR area_m2 IS NOT NULL)
	AND id_imovel != '1'
	AND id_imobiliaria != '1'
	AND id_endereco_imovel != '1'
	AND id_tipo_imovel != '1'
	AND id_modo_imovel != '1'
GROUP BY faixa_area, modo, tipo
ORDER BY 
    CASE faixa_area
        WHEN 'Até 50m²' THEN 1
        WHEN '51-100m²' THEN 2
        WHEN '101-150m²' THEN 3
        WHEN '151-200m²' THEN 4
        WHEN 'Acima de 200m²' THEN 5
        ELSE 6 -- Para valores fora das categorias especificadas
    END;