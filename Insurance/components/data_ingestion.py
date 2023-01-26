import os, sys
import pandas as pd
import numpy as np
from Insurance.entity import config_entity
from Insurance.exception import InsuranceException
from Insurance.entity import artifact_entity
from Insurance import utils
from Insurance.logger import logging
from sklearn.model_selection import train_test_split



class DataIngestion:        #data in to train test and validation 

    def __init__(self,data_ingetion_config:config_entity.DataIngestionConfig):
        try:
            self.data_ingetion_config=data_ingetion_config
        except Exception as e:
            raise InsuranceException(e,sys)

    def intitate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            logging.info("export data as pandas  DataFrame")        
            df:pd.DataFrame = utils.get_collection_as_dataframe(
                database_name=self.data_ingetion_config.database_name,
                collection_name=self.data_ingetion_config.collection_name)
            logging.info("save data in feature store")
            #replace na with NAN
            df.replace(to_replace="na",value=np.NAN,inplace=True)
            #save data in feature store
            logging.info("create feature store folder of not available")

            feature_store_dir=os.path.dirname(self.data_ingetion_config.feature_store_file_path)
            os.makedirs(feature_store_dir,exist_ok=True)

            logging.info("save df to feature store folder ")

            df.to_csv(path_or_buf=self.data_ingetion_config.feature_store_file_path,index=False, header=True)

            logging.info("spliting data into train and test")
            train_df,test_df=train_test_split(df,test_size=self.data_ingetion_config.test_size,random_state=1)

            logging.info("create dataset dir folder if not exists")
            dataset_dir = os.path.dirname(self.data_ingetion_config.train_file_path)
            os.makedirs(dataset_dir, exist_ok=True)

            logging.info("save datatset to feature store folder")
            train_df.to_csv(path_or_buf=self.data_ingetion_config.train_file_path,index=False, header= True)
            test_df.to_csv(path_or_buf=self.data_ingetion_config.test_file_path,index=False, header= True)

            #prepare artifact folder

            data_ingesion_artifact = artifact_entity.DataIngestionArtifact(
                feature_store_file_path=self.data_ingetion_config.feature_store_file_path,
                train_file_path=self.data_ingetion_config.train_file_path,
                test_file_path=self.data_ingetion_config.test_file_path
            )


        except Exception as e:
            raise InsuranceException(e,sys)

        

