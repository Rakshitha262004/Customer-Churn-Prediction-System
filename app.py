import streamlit as st
from src.predict import predict

st.set_page_config(page_title="Churn Dashboard", layout="wide")

# 🌈 CSS Styling
st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: white;
}
.block-container {
    padding: 2rem;
}
.stButton>button {
    background-color: #00C897;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
.card {
    padding: 25px;
    border-radius: 15px;
    background: #1c1f26;
    box-shadow: 0px 0px 15px #000;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("<h1 style='text-align:center;'>📊 Customer Churn Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Predict customer churn using ML</p>", unsafe_allow_html=True)

# LAYOUT
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("👤 Customer Info")
    gender = st.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Partner", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.slider("Tenure", 0, 72, 12)

with col2:
    st.subheader("📡 Services")
    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])

with col3:
    st.subheader("🎬 Extras")
    TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox("Payment Method",
                                ["Electronic check", "Mailed check",
                                 "Bank transfer (automatic)", "Credit card (automatic)"])

# BILLING SECTION
st.markdown("---")
col4, col5 = st.columns(2)

with col4:
    MonthlyCharges = st.slider("💰 Monthly Charges", 0, 150, 70)

with col5:
    TotalCharges = st.slider("💳 Total Charges", 0, 10000, 2000)

# INPUT DICTIONARY (EXACT MATCH)
input_data = {
    "gender": gender,
    "SeniorCitizen": SeniorCitizen,
    "Partner": Partner,
    "Dependents": Dependents,
    "tenure": tenure,
    "PhoneService": PhoneService,
    "MultipleLines": MultipleLines,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection": DeviceProtection,
    "TechSupport": TechSupport,
    "StreamingTV": StreamingTV,
    "StreamingMovies": StreamingMovies,
    "Contract": Contract,
    "PaperlessBilling": PaperlessBilling,
    "PaymentMethod": PaymentMethod,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges
}

# PREDICTION
if st.button("🚀 Predict Churn"):

    prediction, prob = predict(input_data)

    st.markdown("---")

    if prediction == 1:
        st.markdown(f"""
        <div class='card'>
        <h2 style='color:#FF4B4B;'>⚠️ High Churn Risk</h2>
        <h3>Probability: {prob:.2f}</h3>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class='card'>
        <h2 style='color:#00C897;'>✅ Customer Will Stay</h2>
        <h3>Probability: {prob:.2f}</h3>
        </div>
        """, unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown("### 📌 Insights")
st.write("""
- Month-to-month customers are high risk  
- Fiber users churn more  
- Long tenure = loyal customers  
""")