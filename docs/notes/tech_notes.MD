# Anotações Técnicas para elaboração da documentação e execução do script

1.  Para o ambiente virtual conseguir ler a pasta project como um biblioteca python deve configurar o PTHONPATH
~~~bash
export PYTHONPATH=$PYTHONPATH:~./brazilian_ecommerce_data_modeling/project
~~~
2. Caso o export não funcione tente adicionar isso:
~~~python
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
~~~

3. Para conectar o pgAdmin 4 ao PostgreSQL em execução em um contêiner Docker, na guia "Connection" (Conexão) do PgAdmin 4, em "Host name/address" (Nome/endereço do host), insira o nome do serviço do contêiner PostgreSQL ao invês do "localhost" ou "127.0.0.1" como é feito no script Python.

4. No SQLAlchemy, há duas formas de executar consultas SQL, são elas:
- Engine: é uma instância que representa uma conexão com o banco de dados, sendo frequentemente usado para operações de nível mais baixo e para a execução de consultas SQL diretas
~~~python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///example.db')
result = engine.execute("SELECT * FROM my_table")
~~~
- Session: é uma abstração de nível superior que encapsula uma Engine e fornece uma interface mais amigável e orientada a objetos para interagir com o banco de dados, sendo ideal para operações que envolvem transações e manipulação de objetos do banco de dados de maneira mais orientada a objetos
~~~python
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
result = session.execute("SELECT * FROM my_table")
~~~

- Dessa forma, utilizei a Engine para criar as tabelas, e o Session para inserir dados nas tabelas.
