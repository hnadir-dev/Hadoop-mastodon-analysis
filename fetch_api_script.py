from mastodon import Mastodon
import json
from dotenv import load_dotenv
import os
from hdfs import InsecureClient
#from datetime import datetime
import pandas as pd

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
#from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

import subprocess

from insertion_hbase import InsertHbase

# hdfs_folder_path = ""
# hdfs_file_path = ""

global full_path

def taskToFetchAPI():
    today = datetime.today()
    now = datetime.now()

    # #load config env
    load_dotenv()

    hdfs_client = InsecureClient('http://localhost:9870', user='hnadir')

    # Define the HDFS path where you want to save the data
    hdfs_folder_path = f'mastodon_data/{today.strftime("%d-%m-%Y")}'
    hdfs_file_path = f'{str(now.strftime("%H-%M-%S"))}.json'

    #
    
    full_path = f'{hdfs_folder_path}/{hdfs_file_path}'
    
    # #create folder if not exists
    if not hdfs_client.status(hdfs_folder_path, strict=False):
        hdfs_client.makedirs(hdfs_folder_path)


    mastodon = Mastodon(
        client_id=os.getenv('Client_key'),
        client_secret=os.getenv('Client_secret'),
        access_token=os.getenv('Access_token'),
        api_base_url="https://mastodon.social"
    )

    # # Fetch public posts from the federated timeline
    public_posts = mastodon.timeline_public(limit=40) # Adjust the limit as needed

    # Create a text file to store the Mastodon data
    with hdfs_client.write(f'{hdfs_folder_path}/{hdfs_file_path}') as writer:
        items = []
        for post in public_posts:

            items.append(post)

        df = pd.DataFrame(items)

        jsonData = df.to_json(orient='records')
        
        writer.write(jsonData)

def touchText():
    subprocess.run('python3 ./airflow/dags/map_reduce_job.py -r hadoop hdfs:///user/hnadir/mastodon_data/24-10-2023/10-19-19.json > ./airflow/dags/mr_output.txt', shell=True)# 

# Define default arguments for the DAG
default_args = {
    'owner': 'NADIR Hicham',
    'start_date': datetime(2023, 10, 22),
    'retry_dely': timedelta(seconds=10),
    'end_date':None, 
}

# Create a DAG
with DAG('fetch_api_from_mastodon', default_args=default_args, schedule_interval="@once") as dag:#*/1 * * * *
    # Create PythonOperator tasks
    task_1 = PythonOperator(
        task_id='tFetch_data_from_API',
        python_callable=taskToFetchAPI,
    )

    task_2 = PythonOperator(
        task_id='tMapreduce',
        python_callable=touchText,
        dag=dag
    )
    
    task_3 = PythonOperator(
        task_id='InsertionDataInHbaseTask',
        python_callable=InsertHbase.insertDataInHbase,
        dag=dag
    )
    # tasks
    task_1 >> task_2 >> task_3

if __name__ == "__main__":
    dag.cli()
