# coding-guild-aws-hackathon-data

## Building a data pipeline in AWS

Components:
* Ingestion: Lambda
* Datalake: S3
* Data discovery: Glue ETL
* Data dictionary: Glue Catalog
* Data federation: Athena
* Presentation: Quicksight

## Lambda

* can be triggered using time schedule
* query spot instance API
* output json files into S3
* needs IAM role with appropiate permissions 
* python or other language

## S3

* set of buckets containing json
* smart folder structure as the base for metadata retrieval 
* similar to storing files in Hadoop filesystems

## Glue

* determine schema's
* scans folder structure and json files to create data catalog

## Athena

* connects to S3 and Glue Datacatalog
* provides a federated view of underlying data
* can be queried using SQL
* compatible with/provides interface for Hadoop queries 
