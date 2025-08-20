from sqlalchemy import create_engine

# function to create database engine 

def create_db_engine(connection_params):
    try:
        for param in ["dbname", "user", "password", "host", "port"]:
            if not param == "password" and not connection_params.get(param):
                raise ValueError(f"{param} not provided")
        engine = create_engine(
            f"postgresql+psycopg2://{connection_params['user']}"
            f":{connection_params['password']}@{connection_params['host']}"
            f":{connection_params['port']}/{connection_params['dbname']}"
        )
        return engine
    except Exception as e:
        raise ValueError(f"Error creating  database engine: {e}") 
   
# function to get the database connection 
 
def get_db_connection(connection_params):
    try:
        engine = create_db_engine(connection_params)
        connection = engine.connect()
        return connection
    except Exception as e:
        raise ValueError(f"Error connecting to database: {e}")
        