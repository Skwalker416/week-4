import pandas as pd
import os
import zipfile

def load_data(filename, extract_to):
    """
    Load and preprocess data from a compressed archive.
    
    Args:
        filename (str): Path to the zip archive containing the dataset.
        extract_to (str): Directory to extract the data to.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    print(f"Extracting data from {filename} to {extract_to}...")
    
    # Extract the archive
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    # Assume the dataset is a CSV file within the extracted directory
    extracted_files = os.listdir(extract_to)
    csv_file = next((f for f in extracted_files if f.endswith('.csv')), None)

    if not csv_file:
        raise FileNotFoundError("No CSV file found in the extracted archive.")

    # Load the CSV file into a DataFrame
    csv_path = os.path.join(extract_to, csv_file)
    df = pd.read_csv(csv_path)
    print("Data successfully loaded.")
    return df