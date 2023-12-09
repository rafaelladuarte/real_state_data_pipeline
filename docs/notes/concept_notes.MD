# Anotações conceituais

## Normalização dos dados

- O objetivo da normalizaçõa  de dados é remover as anomalias de repetição, atualização, inserção e exclusão.

## Formas Normais

- Primeira Forma Normal (1FN)
    - Possui chave primária;
    - Não possui grupos repetitivos;
    - Todos os seus atributos são atômicos, ou seja, não precisa ser decomposto.
- Segunda Forma Normal (2FN)
    - Está na primeira forma normal;
    - Não possui dependências parciais da chave primária;
- Terceira Forma Normal (3FN)
    - Está na segunda forma normal;
    - Se nenhum dos campos foram determinados transitivamente pela chave primária.

## Esquemas de Banco de Dados

Um esquema de banco de dados refere-se à estrutura lógica ou organização dos dados em um banco de dados. Ele define como os dados são armazenados, organizados e relacionados entre si. O esquema inclui a definição de tabelas, seus campos, tipos de dados, relacionamentos, restrições e outras informações necessárias para representar e armazenar os dados de maneira eficiente. Existem vários tipos de esquemas de banco de dados, e os dois principais são:

- Esquema de Estrela (Star Schema)
    - Usado em ambientes de data warehousing e business intelligence. Divide o banco de dados em tabelas de fatos e dimensões. A tabela de fatos contém métricas (dados quantitativos) e possui chaves estrangeiras que se relacionam com tabelas de dimensões. As tabelas de dimensões contêm informações descritivas sobre os elementos analisados nas métricas.
- Esquema de Floco de Neve (Snowflake Schema):
    - Uma extensão do esquema de estrela que normaliza ainda mais as tabelas de dimensões. Divide as tabelas de dimensões em subdimensões para reduzir a redundância de dados. Cada subdimensão é representada como uma tabela separada com suas próprias chaves primárias e estrangeiras.

A escolha entre um esquema de estrela e um esquema de floco de neve depende dos requisitos específicos do sistema, das consultas que serão executadas com mais frequência e das considerações de desempenho. O esquema de estrela tende a ser mais simples e pode ser mais eficiente para algumas consultas, enquanto o esquema de floco de neve reduz ainda mais a redundância de dados, mas pode exigir mais joins em consultas complexas.