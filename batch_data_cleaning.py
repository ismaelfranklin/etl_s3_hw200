import boto3
import pandas as pd
import io

BUCKET = 'ismael-etl-demo-2025'

def list_csv_files(bucket):
    s3 = boto3.client('s3')
    objects = s3.list_objects_v2(Bucket=bucket).get('Contents', [])
    return [obj['Key'] for obj in objects if obj['Key'].endswith('.csv')]

def load_csv_from_s3(bucket, key):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
    data = response['Body'].read()
    df = pd.read_csv(io.BytesIO(data))
    return df


def process_file(df, file_name):
    df.columns = df.columns.str.strip().str.replace('"', '')
    try:
        mean_height = df['Height(Inches)'].mean()
        min_height = df['Height(Inches)'].min()
        max_height = df['Height(Inches)'].max()
        null_count = df.isnull().sum().sum()
        outliers = df[(df['Height(Inches)'] < 50) | (df['Height(Inches)'] > 90)]
        n_outliers = len(outliers)
    except Exception as e:
        mean_height = min_height = max_height = null_count = n_outliers = 'ERROR'
    
    return {
        'file': file_name,
        'mean_height': mean_height,
        'min_height': min_height,
        'max_height': max_height,
        'missing_values': null_count,
        'outliers': n_outliers
    }

def main():
    summary_list = []
    files = list_csv_files(BUCKET)
    print("Found files:", files)
    for key in files:
        print(f"Processing {key}...")
        try:
            df = load_csv_from_s3(BUCKET, key)
            summary = process_file(df, key)
        except Exception as e:
            summary = {
                'file': key,
                'mean_height': 'ERROR',
                'min_height': 'ERROR',
                'max_height': 'ERROR',
                'missing_values': 'ERROR',
                'outliers': 'ERROR'
            }
        summary_list.append(summary)

    # Create DataFrame from all summaries
    report_df = pd.DataFrame(summary_list)
    print(report_df)
    
    # Save and upload report
    output_csv = 'quality_report.csv'
    report_df.to_csv(output_csv, index=False)
    boto3.client('s3').upload_file(output_csv, BUCKET, output_csv)
    print(f"Uploaded {output_csv} to S3 bucket: {BUCKET}")

if __name__ == '__main__':
    main()
