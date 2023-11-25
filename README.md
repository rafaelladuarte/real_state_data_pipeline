# Project: Brazilian Ecommerce Data Modeling

<p align="center">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/rafaelladuarte/brazilian_ecommerce_data_modeling?style=plastic">
</p>

<p align="center">
<img src="docs/images/ecommerce-brazil.jpg"/>
</p>

<p align="center">
<img src="https://img.shields.io/static/v1?label=Status&message=DESENVOLVIMENTO&color=yellow&style=for-the-badge"/>
</p>

#

<p align="center">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badgeL" />
    <img src="https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badgel" />
    <img src="https://img.shields.io/badge/PostgreSQL-%23316192.svg?style=for-the-badgel"/>
    <img src="https://img.shields.io/badge/sqlAlchemy-F16061?style=for-the-badgel">
	<img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badgeL"/>
</p>

## Objetivo

Criar uma pipeline de ELT na linguagem de programação Python e utilizando o framework osquetrador Apache Aiflow. A etapa de modelagem e transformação de dados será realizada no banco de dados PostgreSQL, de forma a exercitar a linguagem SQL.

## Contexto

A Olist, uma startup brasileira sediada em Curitiba, opera no modelo de negócios de e-commerce, conectando vendedores a compradores em diversas plataformas online. O crescimento significativo nos últimos anos trouxe desafios relacionados ao processamento e armazenamento de dados, impactando a velocidade das análises e atualizações de métricas nos dashboards.

Para enfrentar essas questões, o time de dados da Olist estabeleceu como meta reduzir em 50% o tempo de consulta aos bancos de dados neste trimestre. Como Data Engineer, o objetivo é desenvolver uma solução que otimize a eficiência, proporcionando análises mais rápidas e diminuindo o tempo de atualização das métricas nos dashboards.

## Desafio

A estratégia proposta para reduzir o tempo das consultas no banco de dados envolve a modelagem de dados, seguindo o método de Ralph Kimball descrito no livro "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling". Esse método sugere a criação de tabelas "Fato" para métricas mensuráveis e tabelas "Dimensão" para fornecer dimensionalidade às análises, como data, região, produto e cliente.

O desafio proposto é aplicar essa modelagem aos dados da fonte, criando tabelas "Fato" e "Dimensão". A métrica de sucesso para a solução será a comparação do tempo de execução das consultas entre as tabelas da fonte e o novo modelo de dados. A expectativa é que a nova modelagem otimize significativamente o tempo de consulta, demonstrando a eficácia da abordagem de dimensional modeling. Recomenda-se a leitura do livro sugerido para adquirir conhecimento e prática na técnica.

## Os Dados da Fonte

A fonte de dados são tabelas do sistema de e-commerce da empresa, você pode checar o MER ( Modelo Entidade Relacionamento ) na figura abaixo.

<p align="center">
<img src="images/olist_raw.png"/>
</p>

Os dados estão disponíveis na página do Kaggle:https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce. Você pode ler mais sobre a empresa e também baixar os dados para o seu projeto.

## Etapas do projeto

### Etapa 1 - Extração e Carregamento
- [x] Crie instancias local do MongoDB, Mongo-Express, PostgreSQL, PgAdmin4 e Apache Airflow
- [x] Armazenar dados brutos no MongoDB
- [x] Mapear e Transfir os dados para o PostgreSQL
      
### Etapa 2 - Transformação
- [ ] Identificar Entidades, Relacionamentos e Dimensões
- [ ] Criar do Modelo Entidade-Relacionamento
- [ ] Analisar os Esquemas de Banco de Dados
- [ ] Criar Novo Schema no Banco de Dados
- [ ] Criar Consultas e Views dos dados
      
### Etapa 3 - Análise e Visualização
- [ ] Análise Exploratória
- [ ] Desenvolvimento de Métricas e KPIs
- [ ] Desenvolvimento de Modelos Analíticos (se aplicavel)
- [ ] Desenvolvimento de Dashboards e Relatórios
      
### Etapa 4 - Automatização (Apache Airflow)
- [ ] Automatize a pipeline da Etapa 1
- [ ] Automatize a pipeline da Etapa 2
- [ ] Automatize a pipeline da Etapa 3
      
### Etapa 5 - Documentação
- [ ] Validação dos Resultados
- [ ] Iteração e Ajuste
- [ ] Documentação

## Observações 

Referência de estudo: https://medium.com/@meigarom/como-fazer-um-projeto-de-modelagem-de-dados-para-data-engineering-fde87ca21212


