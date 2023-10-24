# Anotações para execução e documentação

- Para o ambiente virtual conseguir ler a pasta project como um biblioteca python deve configurar o PTHONPATH
~~~bash
export PYTHONPATH=$PYTHONPATH:~./brazilian_ecommerce_data_modeling/project
~~~
- Caso o export não funcione tente adicionar isso:
~~~python
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
~~~

- Para conectar o pgAdmin 4 ao PostgreSQL em execução em um contêiner Docker, na guia "Connection" (Conexão) do PgAdmin 4, em "Host name/address" (Nome/endereço do host), insira o nome do serviço do contêiner PostgreSQL ao invês do "localhost" ou "127.0.0.1" como é feito no script Python.