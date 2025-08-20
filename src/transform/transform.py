import pandas as pd
from src.transform.clean_oscars import clean_oscars
from src.transform.features import create_oscars_features


def transform_data(data):
    try:
        # Clean the data 
        cleaned_oscars = clean_oscars(data)
        # Add features 
        transformed_oscars = create_oscars_features(cleaned_oscars)
        return transformed_oscars
    except Exception as e:
        print(f"Error occurred during trasnformation: {e}")