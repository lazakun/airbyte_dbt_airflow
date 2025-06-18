from datetime import datetime 
from datetime import timedelta
from pathlib import Path
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
import pendulum
import json
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from dbt_airflow.core.config import DbtAirflowConfig
from dbt_airflow.core.config import DbtProfileConfig
from dbt_airflow.core.config import DbtProjectConfig
from dbt_airflow.core.task_group import DbtTaskGroup
from dbt_airflow.operators.execution import ExecutionOperator


CONN_ID = '16765bb4-8a55-4eae-bc3f-c7d122a6e416'

with DAG(
    dag_id="dbt_airbyte_dag", # The name that shows up in the UI
    start_date=pendulum.today(), # Start date of the DAG
    catchup=False,
) as dag:

    # Airbyte synchronization task
    airbyte_sync = AirbyteTriggerSyncOperator(
        task_id='airbyte_postgres',
        airbyte_conn_id='airbyte_conn', # This should be the Airflow connection ID for Airbyte
        connection_id=CONN_ID, # The actual Airbyte connection ID
        asynchronous=False, # Set to True if you want to run it asynchronously
        wait_seconds=3,
        timeout=9680, # Adjust based on your needs
    )
    
    dbt_transform = DbtTaskGroup(
        group_id='transform',
        dbt_project_config=DbtProjectConfig(
            project_path=Path('/opt/airflow/example_dbt_project/'),
            manifest_path=Path('/opt/airflow/example_dbt_project/target/manifest.json'),
        ),
        dbt_profile_config=DbtProfileConfig(
            profiles_path=Path('/opt/airflow/example_dbt_project/profiles'),
            target='dev',
        ),
        dbt_airflow_config=DbtAirflowConfig(
            execution_operator=ExecutionOperator.BASH,
        ),
    )

    airbyte_sync >> dbt_transform