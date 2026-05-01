from src.preprocess import load_data
from src.train import train_and_save

df = load_data("data/Telco-Customer-Churn.csv")

train_and_save(df)