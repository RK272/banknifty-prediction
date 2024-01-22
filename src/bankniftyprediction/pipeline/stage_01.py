from bankniftyprediction.config.configuration import ConfigurationManager
from bankniftyprediction.components.data_ingestion import DataIngestion
from bankniftyprediction.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.move_file()
        
