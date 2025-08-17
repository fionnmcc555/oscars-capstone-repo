import os
import sys
from config.env_config import setup_env
from src.extract.extract import extract_data

def main():
    try:
        # Get the argument from the run_etl command and set up the environment
        setup_env(sys.argv)
        print(
            f"ETL pipeline run successfully in "
            f"{os.getenv('ENV', 'error')} environment!"
        )
        
        # extract data 
        extracted_data = extract_data()
       
        # save extracted data to data/raw 
        extracted_output_path = "data/raw/unclean_oscars.csv"
        os.makedirs(os.path.dirname(extracted_output_path), exist_ok = True)
        extracted_data.to_csv(extracted_output_path, index=False)
       
        # transform data 
    
    except Exception as e:
        raise Exception(f"ETL pipeline failed: {e}")
    
    


if __name__ == "__main__":
    main()
