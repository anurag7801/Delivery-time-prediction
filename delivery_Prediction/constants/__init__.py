import os

ARTIFACT_DIR = "artifact"
FILE_NAME = "raw.csv"


SCHEMA_FILE_PATH = os.path.join(os.getcwd(),"config","schema.yaml")

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


'''
Data validation related constants
'''
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME:str = "report.yaml"
DATA_VALIDATION_VALID_DIR:str = "validated"
DATA_VALIDATION_INVALID_DIR:str = "invalid"