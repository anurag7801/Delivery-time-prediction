import os,sys
from delivery_Prediction.constants import SCHEMA_FILE_PATH
from delivery_Prediction.exception import CustomException
from delivery_Prediction.logging import logger
from delivery_Prediction.entity.config_entity import DataValidationConfig
from delivery_Prediction.entity.artifact_entity import DataValidationArtifact,DataIngestionArtifact
from delivery_Prediction.utils import read_yaml_file,write_yaml_file,read_csv_file
import pandas as pd

class DataValidation:

    def __init__(self,data_ingestion_artifact:DataIngestionArtifact, data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise CustomException(e,sys)
    
    def validate_number_of_columns(self,dataframe:pd.DataFrame)-> bool:
        try:
            number_of_columns = len(self._schema_config['columns'])
            logger.info(f"Required no of columns : [{number_of_columns}]")
            logger.info(f"DataFrame has no of columns : [{len(dataframe.columns)}]")

            if len(dataframe.columns) == number_of_columns:
                return True
            return False
        except Exception as e:
            raise CustomException(e,sys)
        
    def is_numerical_column_present(self,dataframe:pd.DataFrame)-> bool:
        try:
            numerical_columns = self._schema_config['numerical_columns']
            dataframe_columns = dataframe.columns

            numerical_column_present = True
            missing_numerical_columns = []

            for column in numerical_columns:
                if column not in dataframe_columns:
                    numerical_column_present = False
                    missing_numerical_columns.append(column)
            
            logger.info(f"Missing numerical columns: {missing_numerical_columns}")

            return numerical_column_present
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            error_message = ""
            report = {}

            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            train_dataframe = read_csv_file(filepath=train_file_path)
            test_dataframe = read_csv_file(filepath=test_file_path)

            End_status = True

            status = self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message = f"{error_message} Train dataframe does not contain all columns.\n"
            End_status = End_status and status

            status = self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                error_message = f"{error_message} Test dataframe does not contain all columns.\n"
            End_status = End_status and status

            status = self.is_numerical_column_present(dataframe=train_dataframe)
            if not status:
                error_message = f"{error_message} Train dataframe does not contain all numerical columns.\n"
            End_status = End_status and status

            status = self.is_numerical_column_present(dataframe=test_dataframe)
            if not status:
                error_message = f"{error_message} Test dataframe does not contain all numerical columns.\n"
            End_status = End_status and status

            if len(error_message)>0:
                raise Exception(error_message)
            

            data_validation_artifact = DataValidationArtifact(
                validation_status = End_status,
                valid_train_file_path = self.data_ingestion_artifact.trained_file_path,
                valid_test_file_path = self.data_ingestion_artifact.test_file_path,
                invalid_train_file_path = None,
                invalid_test_file_path = None,
                report_path = self.data_validation_config.data_validation_report_path
            )

            logger.info(f"Data Validation Artifact : [{data_validation_artifact}]")

            #for report file
            report.update({"status ":End_status})

            report_file_path = self.data_validation_config.data_validation_report_path
            dir_path = os.path.dirname(report_file_path)
            logger.info(f"Report file path : [{report_file_path}]")
            os.makedirs(dir_path,exist_ok=True)
            write_yaml_file(file_path=report_file_path,content=report,)

            return data_validation_artifact

        except Exception as e:
            raise CustomException(e,sys)