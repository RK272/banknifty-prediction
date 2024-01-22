import os
import urllib.request as request
import shutil
from bankniftyprediction.logging import logger
from bankniftyprediction.utils.common import get_size
from pathlib import Path
from bankniftyprediction.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def move_file(self):
        if not os.path.exists(self.config.local_data_file):
            #create_directories([config.local_data_file])

            N='/config/workspace/1RELIANCE.csv'

            shutil.move(N,'/config/workspace/artifacts/data_ingestion')
           
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

        
    
   