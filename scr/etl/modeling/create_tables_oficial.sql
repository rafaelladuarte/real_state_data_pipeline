CREATE TABLE "Tipo_Imovel" (
  "id_tipo_imovel" SERIAL PRIMARY KEY,
  "tipo" VARCHAR(50) NOT NULL
);

CREATE TABLE "Modo_Imovel" (
  "id_modo_imovel" SERIAL PRIMARY KEY,
  "modo" VARCHAR(50) NOT NULL
);

CREATE TABLE "Endereco" (
  "id_endereco" SERIAL PRIMARY KEY,
  "bairro" VARCHAR(100),
  "cidade" VARCHAR(100) NOT NULL,
  "estado" VARCHAR(2) NOT NULL,
  "cep" VARCHAR(10),
  "rua" VARCHAR(100),
  "numero" INT,
  "complemento" VARCHAR(100),
  "endereco_completo" VARCHAR(250)
);

CREATE TABLE "Imobiliaria" (
  "id_imobiliaria" SERIAL PRIMARY KEY,
  "id_endereco_imobiliaria" INTEGER NOT NULL,
  "nome" VARCHAR(255) NOT NULL,
  "credencial" VARCHAR(100),
  "quantidade_imovel" INTEGER,
  "data_cadastro" DATE,
  "telefone" VARCHAR(20),
  "data_coleta" DATE,
  FOREIGN KEY ("id_endereco_imobiliaria") REFERENCES "Endereco" ("id_endereco")
);

CREATE TABLE "Imovel" (
  "id_imovel" SERIAL PRIMARY KEY,
  "id_imobiliaria" INTEGER NOT NULL,
  "id_endereco_imovel" INTEGER NOT NULL,
  "id_tipo_imovel" INTEGER NOT NULL,
  "id_modo_imovel" INTEGER NOT NULL,
  "titulo" VARCHAR(255) NOT NULL,
  "descricao" TEXT,
  "data_cadastro" DATE,
  "data_atualizacao" DATE,
  "imagens" TEXT[],
  "telefone" TEXT[],
  "preco" DECIMAL(18,2) NOT NULL,
  "quantidade_quartos" INTEGER,
  "quantidade_banheiros" INTEGER,
  "quantidade_vagas" INTEGER,
  "quantidade_suites" INTEGER,
  "area_m2" DECIMAL(10,2),
  "data_coleta" DATE,
  FOREIGN KEY ("id_imobiliaria") REFERENCES "Imobiliaria" ("id_imobiliaria"),
  FOREIGN KEY ("id_endereco_imovel") REFERENCES "Endereco" ("id_endereco"),
  FOREIGN KEY ("id_tipo_imovel") REFERENCES "Tipo_Imovel" ("id_tipo_imovel"),
  FOREIGN KEY ("id_modo_imovel") REFERENCES "Modo_Imovel" ("id_modo_imovel")
);
