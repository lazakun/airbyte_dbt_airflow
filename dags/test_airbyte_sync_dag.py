from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
import pendulum
import json


CONN_ID = '16765bb4-8a55-4eae-bc3f-c7d122a6e416'

with DAG(
    dag_id="test_airbyte_sync_dag", # The name that shows up in the UI
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
        timeout=3680, # Adjust based on your needs
    )
    airbyte_sync