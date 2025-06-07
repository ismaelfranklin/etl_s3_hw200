import boto3
import io
import pandas as pd


def load_csv_from_s3(bucket, key):
    """Download a CSV file from S3 and return a pandas DataFrame."""
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
    data = response['Body'].read()
    df = pd.read_csv(io.BytesIO(data))
    return df

# S3 parameters
bucket = 'ismael-etl-demo-2025'
key = 'hw_200.csv'

# List CSV files in bucket (optional, for demo)
s3 = boto3.client('s3')
files = s3.list_objects_v2(Bucket=bucket).get('Contents', [])
csv_files = [f['Key'] for f in files if f['Key'].endswith('.csv')]
print(csv_files)

# Use your function
df = load_csv_from_s3(bucket, key)

#print the first few rows of the DataFrame
print(df.head())



