from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        # sfp = r"C:\Users\91973\Downloads\ML_Projects\Machine-Learning-Project\config\schema.yaml"
        # fp = r"C:\Users\91973\Downloads\ML_Projects\Machine-Learning-Project\housing\artifact\data_ingestion\2023-02-21-17-50-40\ingested_data\train\housing.csv"
        # df = DataTransformation.load_data(file_path = fp, schema_file_path =sfp)
        # print(df.astype)
        # print(df.columns)
        
    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__=='__main__':
    main()
