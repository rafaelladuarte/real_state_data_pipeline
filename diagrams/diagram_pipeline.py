from diagrams.custom import Custom
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.database import MongoDB
from diagrams.onprem.workflow import Airflow
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.client import User, Client
from diagrams.programming.language import Python

graph_attr = {
    "fontsize": "25",
}

with Diagram(
    "Diagram Real State Data Pipeline",
    filename="diagram_real_state_data_pipeline",
    show=True,
    graph_attr=graph_attr
):
    user = User("Usuário Final")

    with Cluster("Docker"):

        with Cluster("Database"):
            postgres = PostgreSQL("PostgreSQL")
            mongodb = MongoDB("MongoDB")

        with Cluster("Orchestration"):
            airflow = Airflow("Airflow")

        with Cluster("ETL Scripts"):
            python_scraper = Python("1. Extraction")
            python_treatment = Python("2. Treatment")
            sql = Custom("3. Load", "images/sql.png")

    dashboard = Custom("Dashboard", "images/dash_plotly.png")

    web_page = Client("Web Page")

    airflow >> Edge(color="purple", style="bold") \
        >> python_scraper >> Edge(color="darkgreen", style="bold") \
            >> web_page >> Edge(color="darkgreen", style="bold") \
            >> python_scraper >> Edge(color="darkgreen", style="bold") \
            >> mongodb

    airflow >> Edge(color="purple", style="bold") \
        >> python_treatment >> Edge(color="blue", style="bold") \
            >> mongodb >> Edge(color="blue", style="bold") \
            >> python_treatment >> Edge(color="blue", style="bold")

    airflow >> Edge(color="purple", style="bold") \
        >> sql >> Edge(color="red", style="bold") \
            >> mongodb >> Edge(color="red", style="bold") \
            >> sql >> Edge(color="red", style="bold") \
            >> postgres

    postgres >> Edge(color="orange", style="bold") \
        >> dashboard >> Edge(color="orange", style="bold") \
        >> user
