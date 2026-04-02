import json
import logging
import os

DEFAULT_PATH = "data/gradebook.json"
logger = logging.getLogger(__name__)

def load_data(path=DEFAULT_PATH):
    try:
        #open path "r" veq per me bo read
        stream = open(path, "r")
        logger.info(f"Loading data from {path}")
        data = json.load(stream) #Po mujsha me dergu krejt file
        stream.close()
        return data
    except FileNotFoundError:
        logger.info(f"No data file found at {path}, Creating new file.")
        return {"students": [], "courses": [], "enrollments": []}
    except json.JSONDecodeError:
        logger.error(f"Error parsing JSON {path}. Check file format")
        print(f"Error: {path} is not valid. Creating new file.")

def save_data(data, path=DEFAULT_PATH):
    try:
        #Ma mire se os.makedir(path)
        #Po mujka me crash nese path ekziston me os.makedir(path)
        #Nese path eshte i gjate atehere krijon edhe directories tnevojshme zgjidhja me poshte
        os.makedirs(os.path.dirname(path), exist_ok=True)
        stream = open(path, "w")
        json.dump(data, stream)
        stream.close()
        logger.info(f"Data saved to {path}")
    except Exception as e:
        logger.error(f"Data save failed: {e}")
        print(f"Error: Data save failed: {e}")
