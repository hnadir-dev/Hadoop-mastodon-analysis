from mastodon import Mastodon
import json
from dotenv import load_dotenv
import os
from hdfs import InsecureClient
from datetime import datetime
import pandas as pd

today = datetime.today()
now = datetime.now()

#load config env
load_dotenv()

hdfs_client = InsecureClient('http://localhost:9870', user='hnadir')

# Define the HDFS path where you want to save the data
hdfs_folder_path = f'mastodon_data/{today.strftime("%d-%m-%Y")}'
hdfs_file_path = f'{str(now.strftime("%H-%M-%S"))}.json'

#create folder if not exists
if not hdfs_client.status(hdfs_folder_path, strict=False):
    hdfs_client.makedirs(hdfs_folder_path)

mastodon = Mastodon(
    client_id=os.getenv('Client_key'),
    client_secret=os.getenv('Client_secret'),
    access_token=os.getenv('Access_token'),
    api_base_url="https://mastodon.social"
)

# Fetch public posts from the federated timeline
public_posts = mastodon.timeline_public(limit=40) # Adjust the limit as needed


# Create a text file to store the Mastodon data
with hdfs_client.write(f'{hdfs_folder_path}/{hdfs_file_path}') as writer:
    items = []
    for post in public_posts:

        items.append(post)

    df = pd.DataFrame(items)

    jsonData = df.to_json(orient='records')
    
    writer.write(jsonData)

    
    
     


