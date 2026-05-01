import joblib
import pandas as pd

def load_model():
    return joblib.load("models/churn_pipeline.pkl")


def predict(input_dict):
    model = load_model()

    input_df = pd.DataFrame([input_dict])

    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    return prediction, prob