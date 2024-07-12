import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path

from src.logger.logger import logging
from src.exception.exception import customexception
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Initiating Data Ingestion Process.")
            data=pd.read_csv("https://raw.githubusercontent.com/VigneshwarKandhaiya1207/datasets/main/gemstone.csv")
            logging.info("Data successfully fetched from the source.")
            logging.info("Creating the artifacts directory if not exists.")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            logging.info("Writting raw data into {0}".format(self.ingestion_config.raw_data_path))
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Data successfully written to the file.")
            logging.info("Trying to split data as Train and Test")
            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("Train Test split completed.")

            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            logging.info("Data Ingestion completed.")


            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info()
            raise customexception(e,sys)
        


if __name__ == "__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()