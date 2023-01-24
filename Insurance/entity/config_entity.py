import os, sys
from Insurance.exception import InsuranceException
from Insurance.logger import logging
from datetime import datetime

FILE_NAME="insurance.csv"
TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME = "test.csv"


class TrainingPipelineConfig:
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H$M%S')}")
        except Exception as e:
            raise InsuranceException(e,sys)


class DataIngestionConfig:
    def __init__(self,training_pipeling_config: TrainingPipelineConfig):
        try:
            self.database_name="INSURANCE"
            self.collection_name="INSURANCE_PROJECT"
            self.data_ingesion_dir= os.path.join(training_pipeling_config.artifact_dir,"data_ingetion")
            self.feature_store_file_path=os.path.join(self.data_ingesion_dir,"feature_store",FILE_NAME)
            self.train_file_path=os.path.join(self.data_ingesion_dir,"dataset",TRAIN_FILE_NAME) 
            self.test_file_path=os.path.join(self.data_ingesion_dir,"dataset",TEST_FILE_NAME)


        except Exception as e:
            raise InsuranceException(e,sys)


    #CONVER DATA IN DICT
    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise InsuranceException(e,sys)

