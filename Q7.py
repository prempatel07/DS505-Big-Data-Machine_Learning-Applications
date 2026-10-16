"""
PRACTICAL 07: Grouped Aggregations & Action Execution in PySpark
[UNIT 2: Big Data Processing using PySpark]

Problem Statement:
Write a PySpark program to perform grouped aggregations and action executions. Group data by Department using .groupBy(), calculate aggregate metrics (count, average salary, maximum salary, total salary) using pyspark.sql.functions, sort records using .orderBy(), and execute actions (.count(), .show()).

Expected Reference Output:
--- DEPARTMENT-WISE AGGREGATION METRICS ---
+-----------+---------+--------------+----------+-------------+
| Department|Headcount|Average_Salary|Max_Salary|Total_Payroll|
+-----------+---------+--------------+----------+-------------+
|Engineering|        3|       88333.33|     92000|       265000|
|  Marketing|        2|       51000.00|     54000|       102000|
|      Sales|        3|       48666.67|     52000|       146000|
+-----------+---------+--------------+----------+-------------+

Total Unique Departments: 3
Total Records in Dataset : 8
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
from pyspark.sql.functions import col, count, avg, max, sum, round

spark = SparkSession.builder.appName("DS505_Aggregations").master("local[*]").getOrCreate()

# Create department dataset
data = [
    ("Amit", "Sales", 45000),
    ("Pooja", "Engineering", 85000),
    ("Rahul", "Sales", 52000),
    ("Sneha", "Marketing", 48000),
    ("Vikram", "Engineering", 92000),
    ("Ananya", "Marketing", 54000),
    ("Karan", "Sales", 49000),
    ("Riya", "Engineering", 88000)
]
df = spark.createDataFrame(data, ["Employee", "Department", "Salary"])

print("--- INPUT DATASET ---")
df.show()

# GroupBy Aggregation
print("--- DEPARTMENT-WISE AGGREGATION METRICS ---")
dept_summary = df.groupBy("Department").agg(
    count("*").alias("Headcount"),
    round(avg("Salary"), 2).alias("Average_Salary"),
    max("Salary").alias("Max_Salary"),
    sum("Salary").alias("Total_Payroll")
).orderBy(col("Average_Salary").desc())

dept_summary.show()

# Action execution
print(f"Total Unique Departments: {dept_summary.count()}")
print(f"Total Records in Dataset : {df.count()}")

# Stop SparkSession cleanly to release background Java worker processes
spark.stop()
