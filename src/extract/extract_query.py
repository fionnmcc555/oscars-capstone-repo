import pandas as pd 

# Function to extract data from a database using a SQL query

def execute_extract_query(query: str, connection) -> pd.DataFrame:
    try:
        df = pd.read_sql(query, connection)
        return df
    except Exception as e:
        return f"Error executing query: {e}"