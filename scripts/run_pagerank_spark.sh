#!/bin/bash

## CREATE CLUSTER
gcloud dataproc clusters create cluster-a35a --enable-component-gateway --region europe-west1 --zone europe-west1-c --master-machine-type n1-standard-4 --master-boot-disk-size 500 --num-workers 2 --worker-machine-type n1-standard-4 --worker-boot-disk-size 500 --image-version 2.0-debian10 --project master-2-large-scale-data

## COPY PIG CODE
gsutil cp dataproc_spark.py gs://tppascal_bucket/

## CLEAN OUT DIRECTORY
gsutil rm -rf gs://tppascal_bucket/out

## RUN
## SUPPOSE OUT DIRECTORY IS EMPTY
gcloud dataproc jobs submit pyspark --region europe-west1 --cluster cluster-a35a gs://tppascal_bucket/dataproc_spark.py  -- gs://tppascal_bucket/small_page_links.nt 3 results/spark/pagerank_0.out

## ACCESS RESULTS
gsutil cat gs://tppascal_bucket/out/pagerank_data_10/part-r-00000

## DELETE CLUSTER...
gcloud dataproc clusters delete cluster-a35a --region europe-west1