import pandas as pd
from src.extract.extract_oscars import extract_oscars

# function to extract oscars data 

def extract_data():
    try:
        oscars = extract_oscars()
        return oscars
    except Exception as e:
        raise Exception(f"Failed to extract data: {e}")
