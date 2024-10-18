from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime, timedelta
import pandas as pd
import requests
import csv
import os

# Default arguments for the DAG
default_args = {
    'owner': 'pavan',
    'start_date': datetime(2024, 10, 1),
}

# Define the DAG
dag = DAG(
    'extract_insideairbnb_data',
    default_args=default_args,
    description='Download, preprocess, and extract Inside Airbnb data',
    schedule_interval=timedelta(days=1),
)

listing_dates = ["2024-10-14"]

# Task to download CSV file from the API
def download_csv():
    listing_url_template = "https://data.insideairbnb.com/the-netherlands/north-holland/amsterdam/2024-09-05/visualisations/listings.csv"
    os.makedirs('/tmp/insideairbnb', exist_ok=True)  # Ensure directory exists
    for date in listing_dates:
        url = listing_url_template.format(date=date)
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'/tmp/insideairbnb/listing-{date}.csv', 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download {url}")

download_csv_task = PythonOperator(
    task_id='download_csv',
    python_callable=download_csv,
    dag=dag,
)

# Task to preprocess the CSV file
def preprocess_csv():
    for date in listing_dates:
        input_file = f'/tmp/insideairbnb/listing-{date}.csv'
        output_file = f'/tmp/insideairbnb/listing-{date}-processed.csv'
        df = pd.read_csv(input_file)
        df.fillna('', inplace=True)
        df['last_review'].replace('', pd.NaT, inplace=True)
        df.to_csv(output_file, index=False, quoting=csv.QUOTE_ALL)

preprocess_csv_task = PythonOperator(
    task_id='preprocess_csv',
    python_callable=preprocess_csv,
    dag=dag,
)

# Task to upload processed CSV to S3
def upload_to_s3():
    s3_bucket = 'load-data-into-s3'  # Replace with your S3 bucket name
    s3_key_template = 'insideairbnb/listing-{date}-processed.csv'
    
    s3_hook = S3Hook(aws_conn_id='airflow_to_s3')  # Connection ID from Airflow UI
    
    for date in listing_dates:
        file_path = f'/tmp/insideairbnb/listing-{date}-processed.csv'
        s3_key = s3_key_template.format(date=date)
        
        if os.path.exists(file_path):
            s3_hook.load_file(
                filename=file_path,
                bucket_name=s3_bucket,
                key=s3_key,
                replace=True
            )
            print(f"Uploaded {file_path} to s3://{s3_bucket}/{s3_key}")
        else:
            print(f"File {file_path} does not exist")

upload_to_s3_task = PythonOperator(
    task_id='upload_to_s3',
    python_callable=upload_to_s3,
    dag=dag,
)

# Setting task dependencies
download_csv_task >> preprocess_csv_task >> upload_to_s3_task
