import os
import sys
import numpy as np
import pandas as pd
from logger.logger import logging
from exception.exception import customexception
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
