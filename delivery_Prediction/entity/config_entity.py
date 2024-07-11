import os
from datetime import datetime
from delivery_Prediction import constants

class TrainingPipelineConfig:

    def __init__(self,timestamp = datetime.now()):
        timestamp = timestamp.strftime('%d_%m_%Y_%H_%M_%S')
        self.artifact_dir: str = os.path.join(constants.ARTIFACT_DIR,timestamp)

        self.timestamp:str = timestamp


class RawDataConfig:
    def __init__(self):
        self.raw_Data_file_path = os.path.join(constants.RAW_DATA_FILE_DIR, constants.RAW_DATA_FILE_NAME)

class DataIngestionConfig:
    
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        training_pipeline_config = training_pipeline_config

        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, constants.DATA_INGESTION_DIR_NAME)

        self.feature_store_file_path: str = os.path.join(self.data_ingestion_dir, constants.DATA_INGESTION_FEATURE_STORE_DIR_NAME,constants.FILE_NAME)

        self.train_file_path: str = os.path.join(self.data_ingestion_dir,constants.DATA_INGESTION_INGESTED_DIR_NAME,constants.TRAIN_FILE_NAME)

        self.test_file_path: str = os.path.join(self.data_ingestion_dir, constants.DATA_INGESTION_INGESTED_DIR_NAME, constants.TEST_FILE_NAME)

        self.train_test_split_ratio:float = constants.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO


