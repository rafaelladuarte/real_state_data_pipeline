INSERT INTO public."tipo_imovel"(tipo)
VALUES
  	('casas'),
	('apartamentos'),
	('quitinetes'),
	('casas-de-condominio'),
	('cobertura'),
	('flat'),
	('float');

INSERT INTO public."modo_imovel"(modo)
VALUES
  	('comprar'),
	('alugar');

INSERT INTO public."endereco" (
    cidade,
    estado,
    endereco_completo
)
SELECT 
    'Uberlândia' AS cidade,
    'MG' AS estado,
    endereco AS endereco_completo
FROM public._raw_imoveis
UNION ALL
SELECT 
    'Uberlândia' AS cidade,
    'MG' AS estado,
    endereco_imobiliaria AS endereco_completo
FROM public._raw_imobiliarias;

INSERT INTO public.imobiliaria(
	id_imobiliaria,
	id_endereco_imobiliaria,
	nome,
	credencial,
	quantidade_imovel,
	data_cadastro,
	telefone,
	data_coleta
)
SELECT 
	id_imobiliaria,
	B.id_endereco,
	nome_imobiliaria,
	credencial_imobiliaria,
	CAST (quantidade_imovel AS INTEGER),
	TO_DATE(data_cadastro_imobiliaria, 'DD-MM-YYYY'),
	telefone_imobiliaria,
	TO_DATE(data_coleta_imobiliaria, 'DD-MM-YYYY')
FROM public._raw_imobiliarias A
INNER JOIN public.endereco B
	ON A.endereco_imobiliaria = B.endereco_completo


INSERT INTO public."imobiliaria"(
	id_imobiliaria,
	id_endereco_imovel,
	id_tipo_imovel,
	id_modo_imovel,
	titulo,
	descricao,
	data_cadastro,
	imagens,
	telefone,
	preco,
	quantidade_quartos,
	quantidade_banheiros,
	quantidade_vagas,
	quantidade_suites,
	area_m2,
	data_coleta
)
SELECT 
	A.id_imobiliaria,
	B.id_endereco,
	C.id_tipo_imovel,
	D.id_modo_imovel,
	A.titulo_anuncio,
	A.descricao,
	A.data_criacao_anuncio,
	ARRAY_AGG(A.original_imagens),
	ARRAY_AGG(A.telefone),
	A.preco,
	A.quartos,
	A.banheiro,
	A.vagas,
	A.suite,
	A.area,
	A.data_coleta_imovel
FROM public._raw_imobiliarias A
INNER JOIN public."endereco" B
	ON A.endereco_imobiliaria = B.endereco_completo
INNER JOIN 
  public."tipo_imovel" C
  ON LOWER(A.tipo_imovel) = LOWER(C.tipo)
INNER JOIN 
  public."modo_imovel" D
  ON LOWER(A.modo_imovel) = LOWER(D.modo) 


SELECT 
    B.id_imobiliaria,
    C.id_endereco,
    D.id_tipo_imovel,
    E.id_modo_imovel,
    titulo_anuncio,
    descricao,
    TO_DATE(data_criacao_anuncio, 'DD-MM-YYYY'),
    TO_DATE(data_atualizacao_anuncio, 'DD-MM-YYYY'),
    string_to_array(
        REPLACE(
            REPLACE(
                original_imagens, '{', ''
            ),
            '}', ''
        ), ','
    ) AS imagens,
    string_to_array(A.telefone, ',') AS telefone,
    preco,
    quartos,
    banheiro,
    vagas,
    suite,
    area,
    TO_DATE(data_coleta_imovel, 'DD-MM-YYYY')
FROM 
    public._raw_imoveis A
INNER JOIN 
    public.imobiliaria B ON A.id_imobiliaria = B.id_imobiliaria
INNER JOIN 
    public.endereco C ON A.endereco = C.endereco_completo
INNER JOIN 
    public.tipo_imovel D ON LOWER(A.tipo_imovel) = LOWER(D.tipo)
INNER JOIN 
    public.modo_imovel E ON LOWER(A.modo_imovel) = LOWER(E.modo);
