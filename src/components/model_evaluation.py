import os
import sys
import numpy as np
import pandas as pd
from src.logger.logger import logging
from src.exception.exception import customexception
from dataclasses import dataclass

@dataclass
class ModelEvaluationConfig:
    pass

class ModelEvaluation:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)
