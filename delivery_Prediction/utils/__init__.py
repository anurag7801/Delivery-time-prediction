import sys
import pandas as pd
from delivery_Prediction.logging import logger
from delivery_Prediction.exception import CustomException


def read_csv_file(filepath:str) -> pd.DataFrame:
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        raise CustomException(e,sys)