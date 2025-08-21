import pandas as pd 

# function to create new columns in dataset 
def create_oscars_features(oscars):
    assert oscars is not None, "oscars is None entering create_oscars_features"
    oscars = create_main_category_column(oscars)
    oscars = create_decade_column(oscars)
    return oscars

# function to map oscar canonical_category column to main categories
# I used generative AI to help me come up with this function

def map_to_main_category(cat: str) -> str:
    cat_upper = str(cat).upper()
    
    # Picture
    if "PICTURE" in cat_upper and "SHORT" not in cat_upper and "ARTISTIC" not in cat_upper:
        return "Best Picture"
    
    # Director
    if "DIRECTING" in cat_upper:
        return "Best Director"
    
    # Acting
    if "ACTOR" in cat_upper and "SUPPORTING" in cat_upper:
        return "Best Supporting Actor"
    if "ACTRESS" in cat_upper and "SUPPORTING" in cat_upper:
        return "Best Supporting Actress"
    if "ACTOR" in cat_upper:
        return "Best Actor"
    if "ACTRESS" in cat_upper:
        return "Best Actress"
    
    # Writing
    if "WRITING" in cat_upper or "SCREENPLAY" in cat_upper:
        if "ADAPTED" in cat_upper:
            return "Best Adapted Screenplay"
        return "Best Original Screenplay"
    
    # Shorts
    if "SHORT" in cat_upper and "DOCUMENTARY" not in cat_upper and "ANIMATED" not in cat_upper:
        return "Best Live-Action Short Film"
    if "ANIMATED SHORT" in cat_upper:
        return "Best Animated Short Film"
    if "DOCUMENTARY SHORT" in cat_upper:
        return "Best Documentary Short Film"
    
    # Documentary
    if "DOCUMENTARY" in cat_upper:
        if "SHORT" in cat_upper:
            return "Best Documentary Short Film"
        return "Best Documentary Feature Film"
    
    # International
    if "FOREIGN" in cat_upper or "INTERNATIONAL" in cat_upper:
        return "Best International Feature Film"
    
    # Music
    if "SCORE" in cat_upper:
        return "Best Original Score"
    if "SONG" in cat_upper:
        return "Best Original Song"
    
    # Craft
    if "CINEMATOGRAPHY" in cat_upper:
        return "Best Cinematography"
    if "EDITING" in cat_upper:
        return "Best Film Editing"
    if "PRODUCTION DESIGN" in cat_upper or "ART DIRECTION" in cat_upper:
        return "Best Production Design"
    if "COSTUME" in cat_upper:
        return "Best Costume Design"
    if "MAKEUP" in cat_upper or "HAIR" in cat_upper:
        return "Best Makeup & Hairstyling"
    if "SOUND" in cat_upper:
        return "Best Sound"
    if "VISUAL EFFECTS" in cat_upper or "SPECIAL EFFECTS" in cat_upper:
        return "Best Visual Effects"
    
    # Animated Feature
    if "ANIMATED FEATURE" in cat_upper or "ANIMATION" in cat_upper:
        return "Best Animated Feature Film"
    
    # Catch-all
    return "Other / Retired"

# function to create main category column
def create_main_category_column(oscars):
    oscars['main_category'] = oscars['canonical_category'].apply(map_to_main_category)
    return oscars 

# function to create decade column in oscars dataset to group by decade
def create_decade_column(oscars):
    oscars['decade'] = (oscars['award_year'] // 10) * 10
    return oscars 