INSERT INTO public."Tipo_Imovel"(tipo)
VALUES
  	('casas'),
	('apartamentos'),
	('quitinetes'),
	('casas-de-condominio'),
	('cobertura'),
	('flat'),
	('float');

INSERT INTO public."Modo_Imovel"(modo)
VALUES
  	('Comprar'),
	('Alugar');

INSERT INTO public."Endereco"(cidade, estado,endereco_completo)
SELECT 'Uberlândia', 'MG', endereco
	FROM public._raw_imoveis

INSERT INTO public."Endereco"(cidade, estado,endereco_completo)
SELECT 'Uberlândia', 'MG', endereco_imobiliaria
	FROM public._raw_imobiliarias

INSERT INTO public."Imobiliaria"(
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
	quantidade_imovel,
	data_cadastro_imobiliaria,
	telefone_imobiliaria,
	data_coleta_imobiliaria
FROM public._raw_imobiliarias A
INNER JOIN public."Endereco" B
	ON A.endereco_imobiliaria = B.endereco_completo
