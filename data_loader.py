import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path)
        print("Dataset loaded successfully.")
        return df

    except FileNotFoundError:
        print("Dataset not found.")
        return None