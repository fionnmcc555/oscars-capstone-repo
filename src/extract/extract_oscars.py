import os
import pandas as pd
from src.extract.extract_query import execute_extract_query
from src.utils.sql_utils import import_sql_query
from config.db_config import load_db_config
from src.utils.db_utils import get_db_connection

# get file path of the SQL query file 

EXTRACT_OSCARS_QUERY_FILE = os.path.join(
    os.path.dirname(__file__), "../sql/extract_oscars.sql"
    )

# function to extract oscars data from database in pagila 

def extract_oscars():
    try:
        connection_details = load_db_config()["oscars"]
        print(connection_details)
        query = import_sql_query(EXTRACT_OSCARS_QUERY_FILE)
        connection = get_db_connection(connection_details)
        oscars_df = execute_extract_query(query, connection)
        connection.close()
        return oscars_df
    except Exception as e:
        raise Exception(f"Failed to extract data: {e}")
        
        
