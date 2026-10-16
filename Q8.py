"""
PRACTICAL 08: Columnar Storage with Apache Parquet Format in PySpark
[UNIT 2: Big Data Processing using PySpark]

Problem Statement:
Write a PySpark program to demonstrate high-performance columnar storage using Apache Parquet. Create a PySpark DataFrame, export it to Parquet format using .write.mode('overwrite').parquet(), reload the Parquet file using spark.read.parquet(), and verify schema preservation and row counts.

Expected Reference Output:
--- ORIGINAL SENSOR DATAFRAME ---
+---------+-----------+------------+-------------------+
|Sensor_ID|Metric_Type|Metric_Value|          Timestamp|
+---------+-----------+------------+-------------------+
|Sensor_01|Temperature|        24.5|2026-10-10 10:00:00|
|Sensor_02|   Humidity|        65.2|2026-10-10 10:00:00|
...
+---------+-----------+------------+-------------------+
Successfully serialized DataFrame to Parquet storage at: 'sensor_telemetry.parquet'

--- RELOADED FROM PARQUET FORMAT ---
root
 |-- Sensor_ID: string (nullable = true)
 |-- Metric_Type: string (nullable = true)
 |-- Metric_Value: double (nullable = true)
 |-- Timestamp: string (nullable = true)

Verified Record Count: 5 rows.
"""

import os
import sys
import pyspark

# Configure Spark, Python & Java paths explicitly to prevent gateway launch failures
spark_home = os.path.dirname(pyspark.__file__)
os.environ["SPARK_HOME"] = spark_home
os.environ["SPARK_SCALA_VERSION"] = "2.13"
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"

# Resolve and validate JAVA_HOME (clean trailing slashes)
java_candidates = [
    os.environ.get("JAVA_HOME", "").rstrip("/\\"),
    r"C:\Program Files\Microsoft\jdk-17.0.20.101-hotspot",
    os.path.expanduser(r"~\AppData\Local\Java\jdk-17")
]
for jc in java_candidates:
    if jc and os.path.isfile(os.path.join(jc, "bin", "java.exe")):
        os.environ["JAVA_HOME"] = jc
        os.environ["PATH"] = os.path.join(jc, "bin") + os.pathsep + os.environ.get("PATH", "")
        break

# Resolve Hadoop winutils for Windows Parquet support
hadoop_candidates = [
    os.environ.get("HADOOP_HOME", "").rstrip("/\\"),
    os.path.expanduser(r"~\AppData\Local\hadoop")
]
for hc in hadoop_candidates:
    if hc and os.path.isdir(hc):
        os.environ["HADOOP_HOME"] = hc
        os.environ["PATH"] = os.path.join(hc, "bin") + os.pathsep + os.environ.get("PATH", "")
        break

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DS505_Parquet").master("local[*]").getOrCreate()

# Step 1: Create sample IoT sensor telemetry DataFrame
data = [
    ("Sensor_01", "Temperature", 24.5, "2026-10-10 10:00:00"),
    ("Sensor_02", "Humidity", 65.2, "2026-10-10 10:00:00"),
    ("Sensor_01", "Temperature", 25.1, "2026-10-10 10:05:00"),
    ("Sensor_03", "Pressure", 1013.25, "2026-10-10 10:05:00"),
    ("Sensor_02", "Humidity", 64.8, "2026-10-10 10:10:00")
]
columns = ["Sensor_ID", "Metric_Type", "Metric_Value", "Timestamp"]
df = spark.createDataFrame(data, columns)

print("--- ORIGINAL SENSOR DATAFRAME ---")
df.show()

# Step 2: Write to Apache Parquet columnar file format
parquet_path = "sensor_telemetry.parquet"
df.write.mode("overwrite").parquet(parquet_path)
print(f"Successfully serialized DataFrame to Parquet storage at: '{parquet_path}'")

# Step 3: Read back from Parquet format
df_parquet = spark.read.parquet(parquet_path)

print("\n--- RELOADED FROM PARQUET FORMAT ---")
df_parquet.printSchema()
df_parquet.show()

print(f"Verified Record Count: {df_parquet.count()} rows.")

# Stop SparkSession cleanly to release background Java worker processes
spark.stop()
