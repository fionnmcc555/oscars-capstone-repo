import pandas as pd
from src.utils.date_utils import standardise_year

def clean_oscars(oscars):
    oscars = standardise_award_year(oscars)
    oscars = rename_name_column(oscars)
    oscars = drop_multifilmnomination_column(oscars)
    oscars = fill_nulls_in_cols(oscars)
    oscars = drop_duplicates(oscars)
    return oscars 

def standardise_award_year(oscars):
    oscars['award_year'] = oscars['award_year'].apply(standardise_year).dt.year
    return oscars 

def rename_name_column(oscars):
    oscars = oscars.rename(columns={"Name": "name"})
    return oscars

def drop_multifilmnomination_column(oscars):
    oscars = oscars.drop(columns=['multifilmnomination'])
    return oscars

def fill_nulls_in_cols(oscars):
    fill_na_cols = ["name", "film", "nominees", "nominee_ids", "nom_id", "film_id", "detail"]
    oscars[fill_na_cols] = oscars[fill_na_cols].fillna("N/A")
    return oscars

def drop_duplicates(oscars):
    return oscars.drop_duplicates()