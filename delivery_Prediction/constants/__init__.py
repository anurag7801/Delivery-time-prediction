import os

ARTIFACT_DIR = "artifact"
FILE_NAME = "raw.csv"

'''
RAW Data related constants
'''
RAW_DATA_FILE_DIR = "Data"
RAW_DATA_FILE_NAME = "finalTrain.csv"

TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"



'''
Data ingestion constants
'''
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR_NAME:str = "feature_store"
DATA_INGESTION_INGESTED_DIR_NAME:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2