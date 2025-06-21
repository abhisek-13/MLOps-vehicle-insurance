import sys
import pandas as pd
import numpy as np
from typing import Optional

from src.configuration.mongo_db_connection import MongoClient
from src.constants import DATABASE_NAME
from src.exception import MyException

class Proj1Data:
    """
    A class to export MongoDB records as a pandas DataFrame.
    """
    
    def __init__(self) -> None:
      """
        Initializes the MongoDB client connection.
      """
      
      try:
        self.mongo_client = MongoClient(database_name=DATABASE_NAME)
      except Exception as e:
        raise MyException(e, sys)
      
    def export_collection_as_dataframe(self, collection_name:str, database_name: Optional[str] = None) -> pd.DataFrame:
        """
        Exports a MongoDB collection as a pandas DataFrame.

        Parameters:
        ----------
        collection_name : str
            The name of the MongoDB collection to export.
        database_name : Optional[str], optional
            The name of the database. If not provided, uses the default database.

        Returns:
        -------
        pd.DataFrame
            A DataFrame containing the records from the specified MongoDB collection.
        """
        
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            
            print("Fetching data from MongoDB collection...")
            df = pd.DataFrame(list(collection.find()))
            
            print(f"Data fetched with length: {len(df)}")
            if "_id" in df.columns.to_list():
                df.drop(columns=["_id"], axis = 1, inplace=True)
                print("Dropped '_id' column from DataFrame.")
                
            
            df.replace({"na":np.nan}, inplace=True)
            return df
        
        except Exception as e:
            raise MyException(e, sys)