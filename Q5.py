"""
PRACTICAL 05: Apache Spark Session Initialization & DataFrame Schema Inspection
[UNIT 2: Big Data Processing using PySpark]

Problem Statement:
Write a Python program to install and initialize an Apache Spark session in PySpark using SparkSession.builder. Create a structured PySpark DataFrame from Python dictionaries, display its schema tree hierarchy using printSchema(), and print its rows using .show().

Expected Reference Output:
--- SPARK SESSION DETAILS ---
Spark Application Name : DS505_Unit2_Practical5
Spark Version          : 3.5.0
Spark Master Mode      : local[*]

--- PYSPARK DATAFRAME SCHEMA HIERARCHY ---
root
 |-- Emp_ID: string (nullable = true)
 |-- Name: string (nullable = true)
 |-- Department: string (nullable = true)
 |-- Salary: double (nullable = true)
 |-- City: string (nullable = true)

--- PYSPARK DATAFRAME RECORDS (.show) ---
+------+------------+-----------+-------+---------+
|Emp_ID|        Name| Department| Salary|     City|
+------+------------+-----------+-------+---------+
|  E101|Aarav Sharma|Engineering|75000.0|    Surat|
|  E102|  Diya Patel|  Analytics|68000.0|Ahmedabad|
|  E103| Rohan Mehta|Engineering|82000.0|    Surat|
|  E104| Sneha Joshi|  Marketing|54000.0| Vadodara|
|  E105|  Kabir Shah|  Analytics|71000.0|    Surat|
+------+------------+-----------+-------+---------+
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

# Resolve Hadoop winutils for Windows support
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
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# Step 1: Initialize PySpark SparkSession in local cluster mode
spark = SparkSession.builder \
    .appName("DS505_Unit2_Practical5") \
    .master("local[*]") \
    .getOrCreate()

print("--- SPARK SESSION DETAILS ---")
print(f"Spark Application Name : {spark.sparkContext.appName}")
print(f"Spark Version          : {spark.version}")
print(f"Spark Master Mode      : {spark.sparkContext.master}")

# Step 2: Define structured employee data and schema
data = [
    ("E101", "Aarav Sharma", "Engineering", 75000.0, "Surat"),
    ("E102", "Diya Patel", "Analytics", 68000.0, "Ahmedabad"),
    ("E103", "Rohan Mehta", "Engineering", 82000.0, "Surat"),
    ("E104", "Sneha Joshi", "Marketing", 54000.0, "Vadodara"),
    ("E105", "Kabir Shah", "Analytics", 71000.0, "Surat")
]

schema = StructType([
    StructField("Emp_ID", StringType(), True),
    StructField("Name", StringType(), True),
    StructField("Department", StringType(), True),
    StructField("Salary", DoubleType(), True),
    StructField("City", StringType(), True)
])

# Step 3: Create DataFrame and inspect structure
df = spark.createDataFrame(data, schema=schema)

print("\n--- PYSPARK DATAFRAME SCHEMA HIERARCHY ---")
df.printSchema()

print("\n--- PYSPARK DATAFRAME RECORDS (.show) ---")
df.show()

# Stop SparkSession cleanly to release background Java worker processes
spark.stop()
