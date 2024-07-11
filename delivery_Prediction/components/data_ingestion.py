import os,sys
from delivery_Prediction.exception import CustomException
from delivery_Prediction.logging import logger
from delivery_Prediction.entity.artifact_entity import DataIngestionArtifact
from delivery_Prediction.entity.config_entity import DataIngestionConfig,RawDataConfig
from delivery_Prediction.utils import read_csv_file

from pandas import DataFrame
from sklearn.model_selection import train_test_split


class DataIngestion:

    def __init__(self,raw_data_config:RawDataConfig,data_ingestion_config:DataIngestionConfig):
        try:
            self.raw_data_config = raw_data_config
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys)
        
    def export_data_into_feature_store(self) -> DataFrame:
        '''Export dataframe from Data Folder'''

        try:
            logger.info("Exporting data from Data Folder")

            dataframe = read_csv_file(filepath=self.raw_data_config.raw_Data_file_path)

            feature_store_file_path = self.data_ingestion_config.feature_store_file_path

            #creating folder
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)

            dataframe.to_csv(feature_store_file_path, index=False, header= True)

            return dataframe
        except Exception as e:
            raise CustomException(e,sys)
        
    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        try:
            train_set, test_set = train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ratio)
            logger.info("Split data into train and test dataframe")

            dir_path = os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dir_path, exist_ok=True)

            logger.info("Exporting train and test files.")

            train_set.to_csv(self.data_ingestion_config.train_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.test_file_path,index=False, header=True)
            
            logger.info("Exported train and test files.")

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_into_feature_store()
            self.split_data_as_train_test(dataframe=dataframe)
            
            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.train_file_path, test_file_path=self.data_ingestion_config.test_file_path)

            return data_ingestion_artifact
        
        except Exception as e:
            raise CustomException(e,sys)