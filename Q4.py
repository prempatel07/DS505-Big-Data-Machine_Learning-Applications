"""
PRACTICAL 04: Out-of-Core Batch Ingestion & Aggregation via Chunking
[UNIT 1: Introduction to Big Data and Large Dataset Handling]

Problem Statement:
Write a Python program to ingest a large CSV file exceeding single-process RAM in batches using the chunksize parameter of pd.read_csv(). Calculate the cumulative record count, running sum of transaction amounts, and overall average transaction value across all chunks to prevent Out-Of-Memory (OOM) crashes.

Expected Reference Output:
Created 'transactions_stream.csv' with 5,000 records.

--- PROCESSING IN CHUNKS OF 1000 ROWS ---
Chunk 1: Processed 1000 rows | Chunk Sum: $253,420.50 | Running Total: $253,420.50
Chunk 2: Processed 1000 rows | Chunk Sum: $258,110.20 | Running Total: $511,530.70
Chunk 3: Processed 1000 rows | Chunk Sum: $249,850.10 | Running Total: $761,380.80
Chunk 4: Processed 1000 rows | Chunk Sum: $255,200.40 | Running Total: $1,016,581.20
Chunk 5: Processed 1000 rows | Chunk Sum: $252,900.30 | Running Total: $1,269,481.50

--- FINAL AGGREGATION METRICS ---
Total Records Processed : 5,000
Total Cumulative Volume : $1,269,481.50
Overall Average Value   : $253.90
"""

import pandas as pd
import numpy as np

# Step 1: Generate a sample CSV file on disk with 5,000 transaction records
csv_filename = "transactions_stream.csv"
records = 5000

df_temp = pd.DataFrame({
    'Txn_ID': range(1, records + 1),
    'Amount': np.random.uniform(10.0, 500.0, size=records).round(2),
    'Category': np.random.choice(['Retail', 'Dining', 'Travel', 'Utilities'], size=records)
})
df_temp.to_csv(csv_filename, index=False)
print(f"Created '{csv_filename}' with {records:,} records.")

# Step 2: Process the CSV file in chunks to avoid high RAM consumption
chunk_size = 1000
total_records = 0
running_sum = 0.0
chunk_number = 1

print(f"\n--- PROCESSING IN CHUNKS OF {chunk_size} ROWS ---")
for chunk in pd.read_csv(csv_filename, chunksize=chunk_size):
    chunk_count = len(chunk)
    chunk_sum = chunk['Amount'].sum()
    
    total_records += chunk_count
    running_sum += chunk_sum
    
    print(f"Chunk {chunk_number}: Processed {chunk_count} rows | Chunk Sum: ${chunk_sum:,.2f} | Running Total: ${running_sum:,.2f}")
    chunk_number += 1

overall_average = running_sum / total_records
print("\n--- FINAL AGGREGATION METRICS ---")
print(f"Total Records Processed : {total_records:,}")
print(f"Total Cumulative Volume : ${running_sum:,.2f}")
print(f"Overall Average Value   : ${overall_average:.2f}")
