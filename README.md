# Real Estate Data Pipeline

<p align="center">
<img alt="GitHub code size in bytes"  src="https://img.shields.io/github/languages/code-size/rafaelladuarte/real_state_data_pipeline?style=plastic">
<img alt="GitHub repo file count"  src="https://img.shields.io/github/directory-file-count/rafaelladuarte/real_state_data_pipeline?style=plastic">
<img alt="GitHub last commit"  src="https://img.shields.io/github/last-commit/rafaelladuarte/real_state_data_pipeline?style=plastic">
</p>

<img src="images/imoveis.jpeg">

<p align="center">
<img src="https://img.shields.io/static/v1?label=Status&message=Em_Andamento&color=orange&style=for-the-badge"/>
</p>

## Descrição do Projeto

O **Real Estate Data Pipeline** é um projeto de portfólio voltado para a criação de um pipeline de ETL (Extração, Transformação e Carga) para coletar dados de imóveis à venda em sites de imobiliárias de Uberlândia-MG. O objetivo é organizar, transformar e carregar os dados em um banco de dados, permitindo sua visualização em um dashboard interativo no Power BI.

## Objetivo

Este projeto visa automatizar o processo de coleta e análise de dados de imóveis, gerando insights sobre o mercado imobiliário de forma prática e eficiente. O pipeline automatizado irá:

- **Extrair** dados como preço, localização e características dos imóveis a partir de sites de imobiliárias.
- **Transformar** os dados brutos por meio de limpeza e cálculos de insights (ex. preço médio por bairro, variação de preços por características).
- **Carregar** os dados limpos e processados em um banco de dados (PostgreSQL ou MongoDB).
- **Visualizar** os dados por meio de um dashboard interativo, facilitando a análise de tendências no mercado imobiliário.

## Tecnologias Utilizadas

- **Docker**: 
- **Python**: Linguagem principal para desenvolver os scripts de scraping e transformação de dados.
- **Apache Airflow**: Orquestração e gerenciamento do pipeline de ETL.
- **PostgreSQL/MongoDB**: Armazenamento dos dados transformados para consulta e análise.
- **Dash Plotly**: Visualização interativa dos dados e criação de dashboards.
- **Selenium**: Ferramentas para scraping de dados dos sites de imobiliárias.

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

### Parte 1
- ✅ Planejamento e definição de escopo
- ✅ Escolha dos sites de imobiliárias e região alvo
- ✅ Desenho do pipeline de ETL

### Parte 2
- ✅ Configuração do banco de dados MongoDB
- ✅ Desenvolvimento de scripts de scraping para coleta de dados
- ✅ Testes de scraping em massa

Lembrete:
- Implementar coleta de numero de telefone das imobiliarias

### Parte 3
- ✅ Configuração do banco de dados PostgreSQL
- ✅ Migração dados brutos para o PostgreSQL
- ✅ Modelagem de Dados
- ✅ Limpeza e tratamento dos dados brutos
- ✅ Inserção dos dados modelados no banco de dados

### Parte 4
- 🔁 Design e Implementação do Pipeline de ETL no Apache Airflow
- 🔁 Realização de testes manuais do Pipeline de ETL via Interface Web do Apache Airflow
- Monitoramento e Controle do Pipeline por meio de Logs
- Definição de Agendamento Regular para Execução

### Parte 5
- Implementação de funções para cálculo de insights
- Criação de views para os dashboards
- Criação de dashboards interativos

### Parte 6
- Revisão do pipeline e otimização
- Ajustes nos dashboards do Power BI

### Parte 7
- Documentação do projeto
- Preparação do código e documentação para publicação

### Parte 8
- Revisão final
- Gravação de Pitch Técnico
- Publicação do projeto no GitHub

### Parte 9
- Coleta de feedback e ajustes finais

## Contribuições

Este é um projeto de portfólio pessoal, mas contribuições e sugestões são sempre bem-vindas. Sinta-se à vontade para abrir issues ou enviar pull requests!

## Autor

Desenvolvido por Rafaella Duarte.
