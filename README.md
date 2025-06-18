Data Pipeline: MSSQL → Postgres with Airbyte, DBT & Airflow
This repository contains the setup and configurations for a data pipeline that extracts data from Microsoft SQL Server, syncs it to PostgreSQL using Airbyte, transforms it using DBT, and orchestrates the entire process with Airflow in a Docker environment.

Tools & Technologies
•	Airbyte – for extracting and loading data from MSSQL to Postgres.
•	PostgreSQL – serves as the destination and transformation layer.
•	DBT (Data Build Tool) – for transforming raw data into clean models (tables/views).
•	Apache Airflow – for orchestration of the full ETL workflow.
•	Docker – containerization and environment management.

How It Works
1.	Data Sync with Airbyte
Airbyte is configured to extract data from a MSSQL source and load it into a Postgres destination on a scheduled basis.
2.	Transformation with DBT
DBT runs models that transform the synced raw data into meaningful tables and views. The DBT project includes models organized by layer (e.g., staging, intermediate, marts).
3.	Orchestration with Airflow
A custom Airflow DAG handles:
o	Triggering Airbyte syncs
o	Running DBT transformations
o	Monitoring and logging the pipeline execution
4.	Dockerized Environment
All components run in Docker containers for easy setup and deployment.

![dbt drawio](https://github.com/user-attachments/assets/65532f3f-1481-4e1d-89ea-662ff8cd93f2)
