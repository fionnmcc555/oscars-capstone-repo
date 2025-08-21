import pandas as pd
from src.load.load_oscars import load_oscars_data

# function to load in run_etl.py
def load_data(transformed_data):
    load_oscars_data(transformed_data)
    