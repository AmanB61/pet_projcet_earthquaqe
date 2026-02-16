from google.cloud import bigquery
import pandas as pd

client = bigquery.Client.from_service_account_json("/home/aman/keys/bq-key.json")
print("Projcet", client.project)

query = f"""
        SELECT * from PLAYERS.PLAYERS_MMR
"""

df = client.query(query).to_dataframe()
print(df)
datasets = list(client.list_datasets())
if datasets:
    print("Datasets")
    for d in datasets:
        print("-",d.dataset_id)
