import helloworld
import pytest
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import types


# Create some example data
data = [
    ('Batmobile', 7, 5.0),
    ('Batmobile', 2, 0.0),
    ('Batmobile', 3, 5.0),
    ('Catmobile', 7, 5.0),
    ('Catmobile', 2, 5.0),
    ('Catmobile', 3, 9.0),
  
]

custom_schema = types.StructType()
custom_schema.add(types.StructField("my_string", types.StringType()))
custom_schema.add(types.StructField("my_integer", types.IntegerType()))
custom_schema.add(types.StructField("my_float", types.FloatType()))




def test_add():
    assert (helloworld.add(1,1)==2)




    

