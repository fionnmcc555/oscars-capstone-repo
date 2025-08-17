# function to import sql files

def import_sql_query(filename) -> str:
    try:
        with open(filename, 'r') as file:
            imported_query = file.read("\n", " ").strip()
            return imported_query
    except Exception as e:
        return f"Error importing SQL file: {e}"
            