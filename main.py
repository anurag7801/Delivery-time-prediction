import os,sys
from delivery_Prediction.exception import CustomException
from delivery_Prediction.logging import logger
from delivery_Prediction.pipeline.training_pipeline import TrainPipeline


if __name__ == "__main__":
    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()