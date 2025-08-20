import pandas as pd
from sqlalchemy import Connection
from config.db_config import load_db_config, DatabaseConfigError
from src.utils.db_utils import get_db_connection
TABLE_NAME = "cleaned_fm_oscars"

def load_oscars_data(transformed_data):
    connection: Connection | None = None
    try:
        connection_details = load_db_config()['target_database']
        connection = get_db_connection(connection_details)
        
        transformed_data.to_sql(
            TABLE_NAME,
            con=connection,
            schema = "de_2506_a",
            if_exists="append",
            index=False
            
        )
        
        connection.commit()
    
    except DatabaseConfigError as e:
        print(f"Database configuration error: {e}")
    finally:
        if connection and hasattr(connection, 'close'):
            connection.close()
    
        
    
        
