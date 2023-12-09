CREATE TABLE olist.star_schema.geolocalizacao (
	local_id UUID PRIMARY KEY,
	zip_code_prefix INT,
	latitude DOUBLE PRECISION,
	longitude DOUBLE PRECISION,
	cidade VARCHAR(50),
	uf CHAR(2)
);

CREATE TABLE olist.star_schema.vendedor (
	vendedor_id UUID PRIMARY KEY ,
	vendedor_nome VARCHAR(100),
	vendedor_local_id UUID,
	FOREIGN KEY (vendedor_local_id) REFERENCES olist.star_schema.geolocalizacao (local_id)
);

CREATE TABLE olist.star_schema.cliente (
	cliente_id UUID PRIMARY KEY,
	cliente_nome VARCHAR(100),
	cliente_local_id UUID,
	FOREIGN KEY (cliente_local_id) REFERENCES olist.star_schema.geolocalizacao (local_id)
);

CREATE TABLE olist.star_schema.categoria (
	categoria_id UUID PRIMARY KEY,
	categoria_nome VARCHAR(50),
	categoria_hierarquia TEXT
);

CREATE TABLE olist.star_schema.produto (
	produto_id UUID PRIMARY KEY,
	produto_categoria_id UUID,
	produto_nome_tm INT,
	produto_descricao_tm INT,
	produto_fotos_qty INT,
	produto_peso_g INT,
	produto_comprimento_cm INT,
	produto_altura_cm INT,
	produto_largura_cm INT,
	FOREIGN KEY (produto_categoria_id) REFERENCES olist.star_schema.categoria (categoria_id)
);

CREATE TABLE olist.star_schema.item (
	item_id UUID PRIMARY KEY,
	item_limite_qty TIMESTAMP,
	item_preco_vl DOUBLE PRECISION,
	item_frete_vl DOUBLE PRECISION
);

CREATE TABLE olist.star_schema.pagamento (
	pagamento_id UUID PRIMARY KEY,
	pagamento_tipo VARCHAR(20),
	pagamento_seq INT,
	pagamento_parcela INT,
	pagamento_vl DOUBLE PRECISION
);

CREATE TABLE olist.star_schema.comentario (
	comentario_id UUID PRIMARY KEY,
	comentario_nota INT,
	comentario_titulo VARCHAR(100),
	comentario_msg TEXT,
	comentario_criado_dt TIMESTAMP,
	comentario_resp_dt TIMESTAMP
);

CREATE TABLE olist.star_schema.pedido (
	pedido_id UUID PRIMARY KEY,
	cliente_id UUID,
	vendedor_id UUID,
	produto_id UUID, 
	categoria_id UUID,
	comentario_id UUID,
	item_id UUID,
	pagamento_id UUID,
	pedido_status VARCHAR(50),
	pedido_dt TIMESTAMP,
	pedido_aprovado_dt TIMESTAMP,
	pedido_enviado_dt TIMESTAMP,
	pedido_previsao_entrega_dt TIMESTAMP,
	FOREIGN KEY (cliente_id) REFERENCES olist.star_schema.cliente (cliente_id),
	FOREIGN KEY (vendedor_id) REFERENCES olist.star_schema.vendedor (vendedor_id),
	FOREIGN KEY (produto_id) REFERENCES olist.star_schema.produto (produto_id),
	FOREIGN KEY (categoria_id) REFERENCES olist.star_schema.categoria (categoria_id),
	FOREIGN KEY (comentario_id) REFERENCES olist.star_schema.comentario (comentario_id),
	FOREIGN KEY (item_id) REFERENCES olist.star_schema.item (item_id),
	FOREIGN KEY (pagamento_id) REFERENCES olist.star_schema.pagamento (pagamento_id)
);