import pytest
import pandas as pd
from src.extract.extract_oscars import extract_oscars

# used generative AI to help create these functions testing the extraction part of my pipeline

def test_extract_oscars_returns_df():
    df = extract_oscars()
    assert isinstance(df, pd.DataFrame), "Extract did not return a DataFrame"
    
def test_extract_oscars_columns():
    df = extract_oscars()
    expected_columns = {"ceremony",
                        "award_year", 
                        "award_class", 
                        "canonical_category", 
                        "category",
                        "nom_id",
                        "film",
                        "film_id",
                        "Name",
                        "nominees",
                        "nominees_id",
                        "winner",
                        "detail",
                        "mulitfilmnomination"
                        }
    assert expected_columns.issubset(set(df.columns)), "Missing expected columns"
    
    def test_extract_oscars_non_empty():
        df = extract_oscars()
        assert not df.empty, "Extracted DataFrame is empty"