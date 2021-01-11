from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils

spark = SparkSession.builder.getOrCreate()
df= spark.read.parquet("/mnt/raw/staging_nationaldw/dim_sector_ext/src_ref_technology_frequency").show()