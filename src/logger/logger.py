import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

log_file_path=os.path.join(os.getcwd(),"logs")

if not os.path.exists(log_file_path):
    try:
        os.makedirs(log_file_path,exist_ok=True)
    except Exception as e:
        pass
else:
    print("The directoy already exists.")

LOG_FILE_NAME=os.path.join(log_file_path,LOG_FILE)

logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILE_NAME,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")

if __name__== "__main__":
    logging.info("Hi there I am testing.")