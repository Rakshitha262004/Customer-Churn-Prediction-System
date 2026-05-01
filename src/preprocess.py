import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"].fillna(df["TotalCharges"].median(), inplace=True)

    if "customerID" in df.columns:
        df.drop("customerID", axis=1, inplace=True)

    return df