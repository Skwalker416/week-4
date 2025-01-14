from load_data import load_data
from data_preprocessing import preprocess_data
from model_training import train_model

# Define paths for loading and saving data
DATA_ARCHIVE_PATH = "data/data.zip"  # Update with the correct path
EXTRACT_PATH = "data/"      # Directory where the data will be extracted
MODEL_SAVE_PATH = "model/model.pkl"

def main():
    print("Loading data...")
    
    # Load the data by specifying filename and extract_to arguments
    df = load_data(DATA_ARCHIVE_PATH, EXTRACT_PATH)
    
    print("Data loaded. Starting preprocessing...")

    # Preprocess the data
    X, y = preprocess_data(df)

    # Train the model
    print("Training the sales prediction model...")
    model, metrics = train_model(X, y, MODEL_SAVE_PATH)

    print("Model training completed!")
    print(f"Metrics: {metrics}")

if __name__ == "__main__":
    main()
