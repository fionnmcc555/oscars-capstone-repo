import pandas as pd

def test_clean_oscars_matches_expected():
    # load clean csv
    actual = pd.read_csv("data/processed/clean_oscars.csv")   # adjust path as needed

    # load expected oscars clean csv
    expected = pd.read_csv("tests/test_data/expected_oscars_cleaned.csv")

    # assert that they are equal
    pd.testing.assert_frame_equal(
        actual.reset_index(drop=True),
        expected.reset_index(drop=True),
        check_dtype=True
    )