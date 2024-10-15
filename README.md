# Real Estate Data Pipeline

<img src="imoveis.jpeg">

## Descrição do Projeto

O **Real Estate Data Pipeline** é um projeto de portfólio voltado para a criação de um pipeline de ETL (Extração, Transformação e Carga) para coletar dados de imóveis à venda em sites de imobiliárias de Uberlândia-MG. O objetivo é organizar, transformar e carregar os dados em um banco de dados, permitindo sua visualização em um dashboard interativo no Power BI.

## Objetivo

Este projeto visa automatizar o processo de coleta e análise de dados de imóveis, gerando insights sobre o mercado imobiliário de forma prática e eficiente. O pipeline automatizado irá:

- **Extrair** dados como preço, localização e características dos imóveis a partir de sites de imobiliárias.
- **Transformar** os dados brutos por meio de limpeza e cálculos de insights (ex. preço médio por bairro, variação de preços por características).
- **Carregar** os dados limpos e processados em um banco de dados (PostgreSQL ou MongoDB).
- **Visualizar** os dados por meio de um dashboard interativo no Power BI, facilitando a análise de tendências no mercado imobiliário.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para desenvolver os scripts de scraping e transformação de dados.
- **Apache Airflow**: Orquestração e gerenciamento do pipeline de ETL.
- **PostgreSQL/MongoDB**: Armazenamento dos dados transformados para consulta e análise.
- **Power BI**: Visualização interativa dos dados e criação de dashboards.
- **BeautifulSoup e Requests**: Ferramentas para scraping de dados dos sites de imobiliárias.

## Estrutura do Pipeline

1. **Extração de Dados**
   - Coleta de dados de sites de imobiliárias usando scripts de scraping em Python.
   - Paginação automática para garantir a coleta de todos os imóveis disponíveis.
   
2. **Transformação de Dados**
   - Limpeza dos dados brutos: tratamento de valores nulos, formatação de preços e localização.
   - Cálculo de métricas como preço médio por bairro e análise de variações.

3. **Carga de Dados**
   - Armazenamento dos dados limpos em um banco de dados (PostgreSQL ou MongoDB).
   
4. **Visualização**
   - Conexão com o banco de dados para gerar relatórios e dashboards no Power BI.
   - Visualização de insights, como tendências de preços por localização.

## Cronograma de Execução

### Semana 1 (16 a 22 de Outubro)
- Planejamento e definição de escopo
- Escolha dos sites de imobiliárias e região alvo
- Desenho do pipeline de ETL

### Semana 2 (23 a 29 de Outubro)
- Desenvolvimento de scripts de scraping para coleta de dados
- Testes de scraping em diferentes sites de imobiliárias

### Semana 3 (30 de Outubro a 5 de Novembro)
- Limpeza e transformação dos dados brutos
- Implementação de funções para cálculo de insights

### Semana 4 (6 a 12 de Novembro)
- Design e implementação do pipeline de ETL no Apache Airflow
- Integração do scraping e transformação dentro do Airflow

### Semana 5 (13 a 19 de Novembro)
- Configuração do banco de dados (PostgreSQL/MongoDB)
- Inserção dos dados transformados no banco de dados

### Semana 6 (20 a 26 de Novembro)
- Criação de dashboards interativos no Power BI
- Conexão do Power BI ao banco de dados

### Semana 7 (27 de Novembro a 3 de Dezembro)
- Revisão do pipeline e otimização
- Ajustes nos dashboards do Power BI

### Semana 8 (4 a 10 de Dezembro)
- Documentação do projeto
- Preparação do código e documentação para publicação

### Semana 9 (11 a 17 de Dezembro)
- Revisão final
- Publicação do projeto no GitHub

### Semana 10 (18 a 24 de Dezembro)
- Coleta de feedback e ajustes finais

## Contribuições

Este é um projeto de portfólio pessoal, mas contribuições e sugestões são sempre bem-vindas. Sinta-se à vontade para abrir issues ou enviar pull requests!

## Autor

Desenvolvido por [Seu Nome].

