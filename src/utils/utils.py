import os
import sys
import joblib
from pathlib import Path
from logger.logger import logging
from exception.exception import customexception


def save_objects(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            joblib.dump(obj,file_obj)

    except Exception as e:
        raise customexception(e,sys)