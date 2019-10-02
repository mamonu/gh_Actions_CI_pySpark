FROM jupyter/all-spark-notebook:latest
RUN conda install boto3 pytest pytest-cov pytest-xdist pytest-timeout hypothesis hypothesis[pandas] 

RUN pip install gluejobutils
RUN pip install git+git://github.com/moj-analytical-services/etl_manager.git
RUN pip install git+git://github.com/moj-analytical-services/dataengineeringutils.git

COPY pysparkconf.py pysparkconf.py
RUN python pysparkconf.py

ENV PYSPARK_SUBMIT_ARGS  '--packages com.amazonaws:aws-java-sdk:1.10.34,org.apache.hadoop:hadoop-aws:2.6.0 pyspark-shell'

COPY hdfs-site.xml /usr/local/spark/conf

USER root
COPY aptpackages aptpackages
RUN apt-get update 
RUN apt-get install -y $(cat aptpackages)