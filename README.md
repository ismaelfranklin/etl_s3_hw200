# ETL S3 HW200

A hands-on data engineering mini-project: Load, clean, and analyze CSV files from AWS S3 using Python, Pandas, and Boto3.

## 🚀 Project Overview

This project demonstrates a basic data engineering workflow:
- **Extract**: List and load CSV files directly from an AWS S3 bucket.
- **Transform**: Clean and analyze data, perform data quality checks, and generate a report.
- **Load**: Save processed files and reports back to S3.

## 🧰 Tech Stack

- **Python 3.9+**
- **Pandas**
- **Boto3**
- **AWS S3**

## 📂 Project Structure

etl_s3_hw200/

├── batch_data_cleaning.py # Batch data quality checks for all CSVs

├── data_cleaning.py # Data cleaning and basic analysis

├── hw200_with_cm.csv # Sample output CSV (with new columns)

├── main.py # Example: load data from S3

├── quality_report.csv # Data quality report (auto-generated)

├── requirements.txt # Python dependencies

└── README.md #


## 📝 How to Run

1. **Clone this repo**
    ```bash
    git clone https://github.com/YOUR_USERNAME/etl_s3_hw200.git
    cd etl_s3_hw200
    ```

2. **Install dependencies**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Set up your AWS credentials**  
   - You need access to the S3 bucket:
   - Configure with:
     ```bash
     aws configure
     ```
   - Or set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` as environment variables.

4. **Run the scripts**
    - Batch data quality:  
      ```bash
      python batch_data_cleaning.py
      ```

    - Data cleaning & analysis:  
      ```bash
      python data_cleaning.py
      ```

## ✨ Features

- List and process multiple CSV files from S3
- Clean columns and handle missing data
- Outlier detection
- Data summary report (uploaded to S3)
- Example visualization (matplotlib)


**Made with ❤️ by Ismael Franklin | Data Engineering **
