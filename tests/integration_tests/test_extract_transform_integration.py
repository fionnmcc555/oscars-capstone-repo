import pytest
from src.extract.extract import extract_data
from src.transform.transform import transform_data


def test_extract_transform_integration():
    """Integration test: End-to-end extract-transform workflow validation"""
    extracted_data = extract_data()
    result = transform_data(extracted_data)

    # Validate schema and data quality instead of exact match
    expected_columns = {"ceremony",
                        "award_year", 
                        "award_class", 
                        "canonical_category", 
                        "category",
                        "nom_id",
                        "film",
                        "film_id",
                        "name",
                        "nominees",
                        "nominee_ids",
                        "winner",
                        "detail",
                        "main_category",
                        "decade"
                        }
    assert expected_columns.issubset(set(result.columns))
    assert len(result) > 0
    assert result["award_class"].dtype == "object"
    assert result["winner"].dtype == "bool"



def test_extract_transform_performance():
    """Integration test: Performance requirements validation"""
    import time

    start_time = time.time()

    extracted_data = extract_data()
    result = transform_data(extracted_data)

    execution_time = time.time() - start_time
    assert (
        execution_time < 10.0
    ), f"Pipeline took {execution_time:.2f}s, expected <10s"
    assert len(result) > 0, "Pipeline should produce results"


def test_extract_transform_data_volume():
    """Integration test: Validate data processing expectations"""
    extracted_data = extract_data()
    result = transform_data(extracted_data)

    raw_oscars = extracted_data

    # Validate reasonable data processing
    assert len(result) > 0, "Result should not be empty"
    assert len(result) <= len(
        raw_oscars
    ), "Result should not exceed input transactions"
