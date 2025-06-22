import os
import sys
from pandas import DataFrame
import dill
import yaml
import numpy as np

from src.exception import MyException
from src.logger import logging

def read_yaml_file(file_path: str) -> dict:
    try:
      with open(file_path, 'rb') as file:
        return yaml.safe_load(file)
    
    except Exception as e:
      raise MyException(e, sys) from e
    

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
      if replace:
        if os.path.exists(file_path):
          os.remove(file_path)
          
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
          yaml.dump(content, file)
    except Exception as e:
      raise MyException(e, sys) from e
    

def load_object(file_path: str) -> object:
    """
    Returns model/object from project directory.
    file_path: str location of file to load
    return: Model/Obj
    """
    try:
      with open(file_path, 'rb') as file:
        return dill.load(file)
    except Exception as e:
      raise MyException(e, sys) from e
    

def save_object(file_path: str, obj: object) -> None:
    logging.info("Entering the save_object method of utils file.")
    
    try:
      os.makedirs(os.path.dirname(file_path),exist_ok=True)
      with open(file_path, "wb") as file:
        dill.dump(obj, file)
        
      logging.info("Exiting the save_object method fo utils file.")
      
    except Exception as e:
      raise MyException(e,sys) from e
    
def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
      dir_path = os.path.dirname(file_path)
      os.makedirs(dir_path,exist_ok=True)
      with open(file_path, "wb") as file:
        np.save(file, array)
    
    except Exception as e:
      raise MyException(e, sys) from e
    
def load_numpy_array_data(file_path: str, ) -> np.array:
    """
    load numpy array data from file
    file_path: str location of file to load
    return: np.array data loaded
    """
    try:
      with open(file_path, "rb") as file:
        return np.load(file)
    except Exception as e:
      raise MyException(e, sys) from e