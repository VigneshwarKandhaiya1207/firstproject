import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from dataclasses import dataclass
from logger.logger import logging
from exception.exception import customexception

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler,OrdinalEncoder


@dataclass
class DataTransformationConfig:
    pass

class DataTransformation:
    def __init__(self):
        pass

    def initiate_data_transformatica(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)
            
