import pandas as pd
def extract_csv(csv_path):
    csv = pd.read_csv(csv_path)
    print(csv.head())
    return csv