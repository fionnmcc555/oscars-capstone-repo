import pandas as pd

# function to convert the award_year column from string to integer
# this function also handles when the award_year has two values e.g. 1927/28 

def standardise_year(award_year):
    try:
        if isinstance(award_year, str):
            award_year = award_year.strip()
            if '/' in award_year:
                parts = award_year.split('/')
                if len(parts) == 2:
                    base = parts[0][:2]
                    year = int(base + parts[1])
                    return pd.to_datetime(str(year), format='%Y')
            elif '/' not in award_year:
                return pd.to_datetime(award_year, format='%Y')
    
    except Exception as e:
        print(f"Error converting year {award_year}: {e}")

    return pd.NaT        
