#!/bin/bash

## CREATE CLUSTER
## 1 NODE
gcloud dataproc clusters create cluster-a35a --enable-component-gateway --region europe-west1 --zone europe-west1-c --master-machine-type n1-standard-4 --master-boot-disk-size 500 --single-node --worker-machine-type n1-standard-4 --worker-boot-disk-size 500 --image-version 2.0-debian10 --project tppascal
## 2 NODES
gcloud dataproc clusters create cluster-a35a --enable-component-gateway --region europe-west1 --zone europe-west1-c --master-machine-type n1-standard-4 --master-boot-disk-size 500 --num-workers 2 --worker-machine-type n1-standard-4 --worker-boot-disk-size 500 --image-version 2.0-debian10 --project tppascal
## 4 NODES
gcloud dataproc clusters create cluster-a35a --enable-component-gateway --region europe-west1 --zone europe-west1-c --master-machine-type n1-standard-4 --master-boot-disk-size 500 --num-workers 4 --worker-machine-type n1-standard-4 --worker-boot-disk-size 500 --image-version 2.0-debian10 --project tppascal
## 5 NODES
gcloud dataproc clusters create cluster-a35a --enable-component-gateway --region europe-west1 --zone europe-west1-c --master-machine-type n1-standard-4 --master-boot-disk-size 500 --num-workers 5 --worker-machine-type n1-standard-4 --worker-boot-disk-size 500 --image-version 2.0-debian10 --project tppascal

## COPY SPARK CODE
gsutil cp dataproc_spark.py gs://tppascal_bucket/

## CLEAN OUT DIRECTORY
gsutil rm -rf gs://tppascal_bucket/spark-out

## RUN
## SUPPOSE OUT DIRECTORY IS EMPTY
gcloud dataproc jobs submit pyspark --region europe-west1 --cluster cluster-a35a gs://tppascal_bucket/dataproc_spark.py  -- gs://public_lddm_data/page_links_en.nt.bz2 3 gs://tppascal_bucket/spark-out/

## ACCESS RESULTS
gsutil cat gs://tppascal_bucket/spark-out/* > results/small_page_links.nt.out

## DELETE CLUSTER...
gcloud dataproc clusters delete cluster-a35a --region europe-west1