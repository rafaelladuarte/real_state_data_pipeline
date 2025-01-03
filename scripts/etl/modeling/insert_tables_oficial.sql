-- Insere valores na tabela dimensão "tipo_imovel";
INSERT INTO public."tipo_imovel"(tipo)
VALUES
  	('casas'),
	('apartamentos'),
	('quitinetes'),
	('casas-de-condominio'),
	('cobertura'),
	('flat'),
	('float');

-- Insere valores na tabela dimensão "modo_imovel";
INSERT INTO public."modo_imovel"(modo)
VALUES
  	('venda'),
	('aluguel');

-- Insere valores na tabela dimensão "endereco";
INSERT INTO public."endereco" (
	endereco,
	bairro,
    cidade,
    estado,
    rua,
	numero
)
SELECT 
    endereco_completo,
	bairro,
	'Uberlândia',
	'MG',
	COALESCE(rua, 'Não Definido'),
	COALESCE(numero::integer, 0)
FROM public._treat_imoveis
UNION ALL
SELECT 
    endereco_completo,
	bairro,
	'Uberlândia',
	'MG',
	COALESCE(rua, 'Não Definido'),
	COALESCE(numero::integer, 0)
FROM public._treat_imobiliarias;

-- Insere valores na tabela dimensão "imobiliaria";
INSERT INTO public.imobiliaria(
    id_imobiliaria,
    id_endereco_imobiliaria,
    nome_imobiliaria,
    credencial_imobiliaria,
    quantidade_imovel,
    data_cadastro_imobiliaria,
    telefone_imobiliaria,
    data_coleta_imobiliaria
)
SELECT 
    id_imobiliaria,
    B.id_endereco,
    nome_imobiliaria,
    COALESCE(credencial_imobiliaria, 'Não informado'),
    CAST (quantidade_imovel AS INTEGER),
    TO_DATE(data_cadastro, 'DD-MM-YYYY'),
    COALESCE(telefone, 'Não informado'),
    TO_DATE(data_coleta, 'DD-MM-YYYY')
FROM public._treat_imobiliarias A
INNER JOIN public.endereco B
    ON A.endereco_completo = B.endereco
ON CONFLICT (id_imobiliaria) DO NOTHING;
	
-- Insere valores na tabela fato "imovel";
INSERT INTO public.imovel(
    id_imovel,
	id_imobiliaria,
	id_endereco_imovel,
	id_tipo_imovel,
	id_modo_imovel,
	titulo_imovel,
	descricao_imovel,
	data_cadastro_imovel,
	data_atualizacao_imovel,
	imagens_imovel,
	telefone_imovel,
	preco,
	quantidade_quartos,
	quantidade_banheiros,
	quantidade_vagas,
	quantidade_suites,
	outros,
	area_m2,
	data_coleta_imovel
)
SELECT 
    hash,
    B.id_imobiliaria,
    C.id_endereco,
    D.id_tipo,
    E.id_modo,
    titulo_anuncio,
    descricao,
    TO_DATE(data_cadastro, 'DD-MM-YYYY'),
    TO_DATE(data_atualizacao, 'DD-MM-YYYY'),
    string_to_array(
        REPLACE(
            REPLACE(
                imagens, '{', ''
            ),
            '}', ''
        ), ','
    ) AS imagens,
	string_to_array(
        REPLACE(
            REPLACE(
                A.telefone, '{', ''
            ),
            '}', ''
        ), ','
    ) AS telefone,
    preco::INTEGER,
    quartos::INTEGER,
    banheiro::INTEGER,
    vagas::INTEGER,
    suite::INTEGER,
	replace(
	replace(
            replace(outros, '"', ''),
            '{', ''
        ),
        '}', ''
    ) AS outros,
    area::INTEGER,
    TO_DATE(data_coleta_imovel, 'DD-MM-YYYY')
FROM 
    public._treat_imoveis A
INNER JOIN 
    public.imobiliaria B ON A.id_imobiliaria = B.id_imobiliaria
INNER JOIN 
    public.endereco C ON A.endereco_completo = C.endereco
INNER JOIN 
    public.tipo_imovel D ON LOWER(A.tipo_imovel) = LOWER(D.tipo)
INNER JOIN 
    public.modo_imovel E ON LOWER(A.modo_imovel) = LOWER(E.modo)
ON CONFLICT (id_imovel) DO NOTHING;;
