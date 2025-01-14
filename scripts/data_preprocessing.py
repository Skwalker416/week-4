import pandas as pd

def preprocess_data(df):
    """
    Preprocess the dataset for modeling.
    Args:
        df (pd.DataFrame): The input dataset.
    Returns:
        X (pd.DataFrame): Features.
        y (pd.Series): Target variable (Sales).
    """
    print("Starting preprocessing...")
    print("Columns in the dataset:", df.columns)

    # Check if 'CompetitionDistance' exists
    if 'CompetitionDistance' not in df.columns:
        print("CompetitionDistance column missing. Adding placeholder...")
        df['CompetitionDistance'] = -1  # Placeholder value

    # Handle missing values for 'CompetitionDistance'
    df['CompetitionDistance'] = df['CompetitionDistance'].fillna(df['CompetitionDistance'].median())


    # Example preprocessing steps (customize as needed)
    # Extract features, encode categorical variables, etc.
    
    # Example feature and target split
    X = df.drop(columns=['Sales', 'Date'], errors='ignore')  # Adjust based on your dataset
    y = df['Sales'] if 'Sales' in df.columns else None

    print("Preprocessing complete. Returning X and y.")
    return X, y
