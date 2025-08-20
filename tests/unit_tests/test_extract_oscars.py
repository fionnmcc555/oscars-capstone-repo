import pandas as pd
import src.extract.extract_oscars as mod

# Tiny fake connection with a .close() so your code doesn't crash
class FakeConn:
    def __init__(self):
        self.closed = False
    def close(self):
        self.closed = True

def test_extract_oscars_returns_dataframe(mocker):
    # Mock external deps so no real env/DB is needed
    mocker.patch.object(mod, "load_db_config", return_value={"source_database": {}})
    mocker.patch.object(mod, "import_sql_query", return_value="SELECT ...")  # path isn't used in test
    fake_conn = FakeConn()
    mocker.patch.object(mod, "get_db_connection", return_value=fake_conn)

    # Return a DF that matches your query columns exactly
    mock_df = pd.DataFrame({
        "ceremony": [67],
        "award_year": [1995],
        "award_class": ["Feature Film"],
        "canonical_category": ["Best Picture"],
        "category": ["Best Picture"],
        "nom_id": ["1234"],
        "film": ["Forrest Gump"],
        "film_id": ["5678"],
        "Name": ["Forrest Gump"],       
        "nominees": ["Forrest Gump"],
        "nominee_ids": ["123"],          
        "winner": [True],
        "detail": ["Some detail"],
        "multifilmnomination": [False],
    })
    mocker.patch.object(mod, "execute_extract_query", return_value=mock_df)

    df = mod.extract_oscars()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert fake_conn.closed  # ensure .close() was called

def test_extract_oscars_columns(mocker):
    mocker.patch.object(mod, "load_db_config", return_value={"source_database": {}})
    mocker.patch.object(mod, "import_sql_query", return_value="SELECT ...")
    fake_conn = FakeConn()
    mocker.patch.object(mod, "get_db_connection", return_value=fake_conn)

    mock_df = pd.DataFrame({
        "ceremony": [67],
        "award_year": [1995],
        "award_class": ["Feature Film"],
        "canonical_category": ["Best Picture"],
        "category": ["Best Picture"],
        "nom_id": [1234],
        "film": ["Forrest Gump"],
        "film_id": [5678],
        "Name": ["Forrest Gump"],     
        "nominees": ["Forrest Gump"],
        "nominee_ids": ["123"],
        "winner": [True],
        "detail": ["Some detail"],
        "multifilmnomination": [False],
    })
    mocker.patch.object(mod, "execute_extract_query", return_value=mock_df)

    df = mod.extract_oscars()

    expected_cols = [
        "ceremony",
        "award_year",
        "award_class",
        "canonical_category",
        "category",
        "nom_id",
        "film",
        "film_id",
        "Name",             
        "nominees",
        "nominee_ids",
        "winner",
        "detail",
        "multifilmnomination",
    ]
    assert list(df.columns) == expected_cols
    assert fake_conn.closed
