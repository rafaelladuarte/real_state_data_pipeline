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