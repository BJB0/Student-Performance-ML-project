from src.DataScienceProject.logger import logging
from src.DataScienceProject.exception import CustomException,sys


if __name__ =="__main__":
  logging.info("The execution has started")
  
  
  try:
    a=1/0
  except Exception as e:
    logging.info('Divide by zero Error')
    raise CustomException(e,sys)