import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from dataclasses import dataclass
from logger.logger import logging
from exception.exception import customexception
from utils.utils import save_objects


@dataclass
class ModelTrainerConfig:
    pass

class ModelTrainer:
    def __init__(self):
        pass

    def initiate_model_training(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)