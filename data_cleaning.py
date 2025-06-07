
# Libraries
import io
import boto3
import pandas as pd
import matplotlib.pyplot as plt


# Setting up the S3
bucket = 'ismael-etl-demo-2025'
key = 'hw_200.csv'

#create the S3 client
s3 = boto3.client('s3')
response = s3.get_object(Bucket=bucket, Key=key)
data = response['Body'].read() 

df = pd.read_csv(io.BytesIO(data))

# Clean column names
df.columns = df.columns.str.strip().str.replace('"', '')
print(df.columns)  # Check the new names

# Convert Height(Inches) to Height_CM
df['Height_CM'] = df['Height(Inches)'] * 2.54
print(df[['Height(Inches)', 'Height_CM']].head())


# Find suspicious values
outliers = df[(df['Height(Inches)'] < 50) | (df['Height(Inches)'] > 90)]
print(outliers)

print("Descriptive statistics for Height and Weight:")
print(df[['Height(Inches)', 'Weight(Pounds)', 'Height_CM']].describe())

# Save the cleaned DataFrame to a new CSV file
output_csv = 'hw200_with_cm.csv'
df.to_csv(output_csv, index=False)
s3.upload_file(output_csv, bucket, output_csv)

# analyzing the data
plt.hist(df['Height_CM'], bins=20)
plt.title('Height Distribution in CM')
plt.xlabel('Height (CM)')
plt.ylabel('Frequency')
plt.show()
