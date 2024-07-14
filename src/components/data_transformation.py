import os
import sys
import numpy as np
import pandas as pd
from pathlib import Path
from dataclasses import dataclass
from src.logger.logger import logging
from src.exception.exception import customexception
from src.utils.utils import save_objects

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler,OrdinalEncoder


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_tansformation_config=DataTransformationConfig()
    
    def get_data_transformatica(self):
        try:
            logging.info("Building the Preprocessor Pipeline.")
            categorical_cols = ['cut', 'color','clarity']
            numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
                   
            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())

                ]

            )
            
            # Categorigal Pipeline
            cat_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                ('scaler',StandardScaler())
                ]
            )           
            
            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_cols),
            ('cat_pipeline',cat_pipeline,categorical_cols)
            ])
            
            return preprocessor
            

        except Exception as e:
            logging.info("Data Transformation Pipeline building failed.")
            raise customexception(e,sys)

    def initiate_data_transformatica(self,train_path,test_path):
        try:
            logging.info("Reading the training data.")
            train_data=pd.read_csv(train_path)
            logging.info("Completed reading the Training data.")
            logging.info("Reading the test data.")
            test_data=pd.read_csv(test_path)
            logging.info("Completed reading the Testing data.")

            logging.info("Training Data: {}\n".format(train_data.head().to_string()))
            logging.info("Testing Data: {}\n".format(test_data.head().to_string()))

            preprocessing_obj=self.get_data_transformatica()
            logging.info("Preprocessor Pipeline is ready to be used.")

            target_column_name = 'price'
            drop_columns = [target_column_name,'id']
            
            input_feature_train_df = train_data.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_data[target_column_name]
            
            
            input_feature_test_df=test_data.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_data[target_column_name]
            
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            
            logging.info("Applying preprocessing object on training and testing datasets.")
            
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_objects(
                file_path=self.data_tansformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr
            )
            
        except Exception as e:
            logging.info("Data Transformation Pipeline failed to complete.")
            logging.info("Error occurred during the initiate_datatransformation.")
            raise customexception(e,sys)
