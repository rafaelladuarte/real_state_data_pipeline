-- Tabela para armazenar tipos de imóveis (ex.: apartamento, casa)
CREATE TABLE "tipo_imovel" (
  "id_tipo_imovel" SERIAL PRIMARY KEY,
  "tipo" VARCHAR(50) NOT NULL UNIQUE
);

-- Tabela para armazenar modos de imóveis (ex.: comprar, alugar)
CREATE TABLE "modo_imovel" (
  "id_modo_imovel" SERIAL PRIMARY KEY,
  "modo" VARCHAR(50) NOT NULL UNIQUE
);

-- Tabela para armazenar endereços de imóveis
CREATE TABLE "endereco" (
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

-- Tabela para armazenar dados de imobiliárias
CREATE TABLE "imobiliaria" (
  "id_imobiliaria" SERIAL PRIMARY KEY,
  "id_endereco_imobiliaria" INTEGER NOT NULL,
  "nome" VARCHAR(255) NOT NULL,
  "credencial" VARCHAR(100),
  "quantidade_imovel" INTEGER DEFAULT 0,
  "data_cadastro" DATE DEFAULT CURRENT_DATE,
  "telefone" VARCHAR(20),
  "data_coleta" DATE,
  FOREIGN KEY ("id_endereco_imobiliaria") REFERENCES "endereco" ("id_endereco")
);

-- Tabela para armazenar informações sobre imóveis
CREATE TABLE "imovel" (
  "id_imovel" SERIAL PRIMARY KEY,
  "id_imobiliaria" INTEGER NOT NULL,
  "id_endereco_imovel" INTEGER NOT NULL,
  "id_tipo_imovel" INTEGER NOT NULL,
  "id_modo_imovel" INTEGER NOT NULL,
  "titulo" VARCHAR(255) NOT NULL,
  "descricao" TEXT,
  "data_cadastro" DATE DEFAULT CURRENT_DATE,
  "data_atualizacao" DATE DEFAULT CURRENT_DATE,
  "imagens" TEXT[],
  "telefone" TEXT[],
  "preco" DECIMAL(18,2) NOT NULL,
  "quantidade_quartos" INTEGER DEFAULT 0,
  "quantidade_banheiros" INTEGER DEFAULT 0,
  "quantidade_vagas" INTEGER DEFAULT 0,
  "quantidade_suites" INTEGER DEFAULT 0,
  "area_m2" DECIMAL(10,2),
  "data_coleta" DATE,
  FOREIGN KEY ("id_imobiliaria") REFERENCES "imobiliaria" ("id_imobiliaria"),
  FOREIGN KEY ("id_endereco_imovel") REFERENCES "endereco" ("id_endereco"),
  FOREIGN KEY ("id_tipo_imovel") REFERENCES "tipo_imovel" ("id_tipo_imovel"),
  FOREIGN KEY ("id_modo_imovel") REFERENCES "modo_imovel" ("id_modo_imovel")
);

-- Índices sugeridos para melhorar o desempenho
CREATE INDEX idx_endereco_cidade ON "endereco" ("cidade");
CREATE INDEX idx_imobiliaria_nome ON "imobiliaria" ("nome");
CREATE INDEX idx_imovel_preco ON "imovel" ("preco");
