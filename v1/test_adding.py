import helloworld
import pytest
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import types
sc = SparkContext.getOrCreate()
spark = SparkSession(sc)



# Create some example data
data = [
    ('Batmobile', 7, 5.0),
    ('Catmobile', 3, 9.0),
    ('', 4, 21.0),
]

custom_schema = types.StructType()
custom_schema.add(types.StructField("Vehicle", types.StringType()))
custom_schema.add(types.StructField("wheels", types.IntegerType()))
custom_schema.add(types.StructField("speed", types.FloatType()))


df = spark.createDataFrame(data, custom_schema)

def test_add():
    assert (helloworld.add(1,1)==2)


def test_data_count_check():
    assert (df.count()==3)

    

