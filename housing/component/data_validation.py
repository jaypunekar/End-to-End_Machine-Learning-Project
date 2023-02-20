from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact    
import os, sys

class DataValidation:

    def __init__(
        self,
        data_validation_config: DataValidationConfig,
        data_ingestion_artifact: DataIngestionArtifact
    ):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e, sys) from e

    def is_train_test_file_exists(self) -> bool:
        try:
            logging.info("Checking is train and test files are available")
            is_train_file_exist = False
            is_test_file_exist = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_available = is_test_file_exist and is_train_file_exist

            logging.info(f"Is train and test file available? -> {is_available}")

            if not is_available:
                train_file = self.data_ingestion_artifact.train_file_path
                test_file = self.data_ingestion_artifact.test_file_path

                message = f"Training file: {train_file} or Testing file: {test_file} not present"
                logging.error(message)
                raise Exception(message)
            return is_available
        except Exception as e:
            raise HousingException(e, sys) from e
    
    def valiadate_dataset_schema(self) -> bool:
        try:
            validation_status = False

            # Assignment
            # Validate Train and Test dataset using schema file
            # 1. Number of columns
            # 2. Check the values of ocean proximity
            # 3. Check column names
            validation_status = True
            return validation_status
        except Exception as e:
            raise HousingException(e, sys) from e

    def initaite_data_validation(self):
        try:
            self.is_train_test_file_exists()
            self.valiadate_dataset_schema() 

        except Exception as e:
            raise HousingException(e, sys) from e