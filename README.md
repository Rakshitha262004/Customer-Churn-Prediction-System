# 📊 Customer Churn Prediction System

An end-to-end Machine Learning project that predicts whether a customer is likely to churn based on their behavior, services, and billing data.

---

## 🚀 Project Overview

Customer churn is a major problem in industries like telecom, banking, and SaaS. This project builds a predictive model to identify customers who are likely to leave.

### 🎯 Objectives:

* Predict customer churn (Yes/No)
* Help businesses reduce customer loss
* Enable targeted retention strategies

---

## 🧠 Business Use Case

Companies use churn prediction to:

* 🔹 Identify high-risk customers
* 🔹 Offer personalized discounts
* 🔹 Improve customer satisfaction
* 🔹 Increase revenue and retention

---

## ⚙️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
* **Model:** Random Forest Classifier
* **Frontend:** Streamlit
* **Model Saving:** Joblib

---

## 📂 Project Structure

```
Customer-Churn-Prediction/
│
├── data/
├── src/
├── models/
├── outputs/
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

* Telco Customer Churn Dataset
* Includes:

  * Demographics
  * Services used
  * Billing details
  * Churn label

👉 Download: https://www.kaggle.com/blastchar/telco-customer-churn

---

## 🔄 Workflow

```
Raw Data → Preprocessing → Feature Engineering → Model Training → Prediction → Dashboard
```

---

## 🤖 Machine Learning Pipeline

* Data Cleaning (missing values handling)
* Encoding categorical variables
* Feature scaling
* Model training using Random Forest
* Evaluation using confusion matrix & accuracy

---

## 📈 Model Performance

* Accuracy: ~80% (varies slightly)
* Evaluation Metrics:

  * Precision
  * Recall
  * F1-score

---

## 🖥️ Streamlit Dashboard

The project includes an interactive web app where users can:

* Enter customer details
* Predict churn probability
* View results instantly

---

## 🎥 Demo Video

👉 Watch the full project demo here:
[![Watch Demo](https://img.shields.io/badge/Watch-Demo-blue)](YOUR_VIDEO_LINK_HERE)

---

## 📸 Screenshots

### Dashboard UI

![Dashboard](images/dashboard.png)

### Prediction Result

![Prediction](images/result.png)

### Confusion Matrix

![Confusion](outputs/confusion_matrix.png)

---

## ▶️ How to Run

### 1. Clone Repository

```
git clone https://github.com/your-username/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Train Model

```
python main.py
```

### 5. Run App

```
streamlit run app.py
```

---

## 💡 Key Insights

* Customers with **month-to-month contracts** are more likely to churn
* **Higher monthly charges** increase churn probability
* Customers with **long tenure** are less likely to churn

---

## 📌 Future Improvements

* Add deep learning models
* Deploy using cloud (Render / AWS)
* Add real-time database
* Improve UI with analytics dashboard

---

## 👩‍💻 Author

Rakshitha A S
BE Cyber Security Student

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
