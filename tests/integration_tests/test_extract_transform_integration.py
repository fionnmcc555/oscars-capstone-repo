import pytest
from src.extract.extract import extract_data
from src.transform.transform import transform_data

# integration tests for the extract-transform pipeline
def test_extract_transform_integration():
    extracted_data = extract_data()
    result = transform_data(extracted_data)
    
    # validate result 
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


# tests time taken for extract-transform part of pipeline
def test_extract_transform_performance():
    import time

    start_time = time.time()

    extracted_data = extract_data()
    result = transform_data(extracted_data)

    execution_time = time.time() - start_time
    assert (
        execution_time < 10.0
    ), f"Pipeline took {execution_time:.2f}s, expected <10s"
    assert len(result) > 0, "Pipeline should produce results"

# tests that the data volume during extract-transform is reasonable
def test_extract_transform_data_volume():
    extracted_data = extract_data()
    result = transform_data(extracted_data)

    raw_oscars = extracted_data

    # validate reasonable data processing
    assert len(result) > 0, "Result should not be empty"
    assert len(result) <= len(
        raw_oscars
    ), "Result should not exceed input oscars"
