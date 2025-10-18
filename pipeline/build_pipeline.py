from src.data_loader import AnimeDataLoader


from src.vector_stores import VectorStoreBuilder
from dotenv import load_dotenv

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.data_loader import AnimeDataLoader


from utils.logger import get_logger
from utils.custom_exception import CustomException


logger=get_logger(__name__)
def main():
    try:
        logger.info("Starting to build the main pipeline")
        loader=AnimeDataLoader('data/anime_with_synopsis.csv','data/updated_anime.csv')
        processed_csv=loader.load_and_process()
        logger.info("Data loaded and processed...")
        vector_builder=VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vectorstores()
        logger.info("vector store built succesfully...")
    except Exception as e:
        logger.error(f"Failed to execute the pipeline {e}")
        raise CustomException("Error during peipeline initialization",e)

if __name__=="__main__":
    main()


