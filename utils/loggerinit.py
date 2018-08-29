import logging
import os.path
 
def initialize_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    
    handler = logging.StreamHandler()
    handler.setLevel(logging.ERROR)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    handler = logging.FileHandler(f"{os.getcwd()}\\logs\\core.log","w", encoding=None, delay="true")
    handler.setLevel(logging.CRITICAL)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
 
