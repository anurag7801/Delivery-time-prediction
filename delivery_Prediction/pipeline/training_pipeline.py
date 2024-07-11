import sys
from delivery_Prediction.exception import CustomException
from delivery_Prediction.logging import logger
from delivery_Prediction.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from delivery_Prediction.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,RawDataConfig,DataValidationConfig
from delivery_Prediction.components.data_ingestion import DataIngestion
from delivery_Prediction.components.data_validation import DataValidation


class TrainPipeline:

    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
        self.raw_data_config = RawDataConfig()
    
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)

            logger.info("Starting Data Ingestion")

            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config,raw_data_config=self.raw_data_config)

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logger.info(f"Data ingestion complete and artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)-> DataValidationArtifact:
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact, data_validation_config=data_validation_config)
            
            data_validation_artifact = data_validation.initiate_data_validation()

            return data_validation_artifact


        except Exception as e:
            raise CustomException(e,sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
        
        except Exception as e:
            raise CustomException(e,sys)