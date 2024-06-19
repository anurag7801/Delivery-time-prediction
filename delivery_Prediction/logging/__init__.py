import logging
import os,sys
from datetime import datetime

LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

os.makedirs(LOG_DIR, exist_ok=True)

# log_2024_06_19_24_05_03.log
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

file_name = f"log_{CURRENT_TIME_STAMP}.log"

log_file_path = os.path.join(LOG_DIR,file_name)

logging.basicConfig(filename=log_file_path,
                    filemode="w",
                    format = '[%(asctime)s] %(name)s - %(levelname)s -%(message)s',
                    level= logging.INFO
                    )

logger = logging.getLogger()
