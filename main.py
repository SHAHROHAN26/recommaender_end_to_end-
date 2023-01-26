from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os,sys
from Insurance.utils import get_collection_as_dataframe
from Insurance.entity.config_entity import DataIngestionConfig
from Insurance.entity import config_entity
from Insurance.components.data_ingestion import DataIngestion



'''def test_logger_and_exception():
    try:
        logging.info("Starting the test_logger_and_exception")
        result = 3/0
        print(result)
        logging.info("Stoping the test_logger_and_exception")
    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(e, sys)'''  #this is just to check logging 

if __name__=="__main__":
    try:
        #test_logger_and_exception()
        #get_collection_as_dataframe(database_name="INSURANCE", collection_name="INSURANCE_PROJECT")

        training_pipeling_config=config_entity.TrainingPipelineConfig()
        data_ingetion_config = config_entity.DataIngestionConfig(training_pipeling_config=training_pipeling_config)
        print(data_ingetion_config.to_dict())

        data_ingesion= DataIngestion(data_ingetion_config=data_ingetion_config)
        data_ingesion_artifact= data_ingesion.intitate_data_ingestion()

    except Exception as e:
        print(e)
        