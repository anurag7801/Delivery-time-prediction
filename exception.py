from delivery_Prediction.logging import logger
from delivery_Prediction.exception import CustomException
import os, sys

try:
    a = 10
    b = 20
    c = a+b
    d = a/0
except Exception as e:
    ml = CustomException(e,sys)
    logger.info(ml.error_message)