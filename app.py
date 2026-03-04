import os
import streamlit as st
import joblib

os.system("clear")

print("hello world")

# Check streamlit version
print(f"Streamlit version: {st.__version__}")

# Set page configuration
st.set_page_config(page_title="Telco Churn Dashboard", layout="wide")

st.title("📊 Telco Customer Churn Prediction Dashboard")
st.write("This dashboard predicts whether a customer is likely to churn.")

# Ensure model directory and files exist before loading
model_dir = "model"
model_path = os.path.join(model_dir, "churn_model.pkl")
scaler_path = os.path.join(model_dir, "scaler.pkl")

if not os.path.isdir(model_dir):
    st.error(f"Required directory '{model_dir}' not found. Please run the training notebook to create it.")
    st.stop()

if not os.path.isfile(model_path) or not os.path.isfile(scaler_path):
    st.error(
        f"Model files not found. Expected:\n  {model_path}\n  {scaler_path}\n"
        "Please rerun the training notebook to generate them."
    )
    st.stop()

# Load trained model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Sidebar for navigation
page = st.sidebar.selectbox(
    "Select Page",
    ["Home", "Data Overview", "Make Prediction"]
)


# # Display Home page content
# if page == "Home":
#     st.header("Project Overview")
#     st.write("""
#     This project analyses telecom customer behaviour and predicts churn risk
#     using machine learning.
#     """)


# # Display Data Overview page
#     elif page == "Data Overview":
#     df = pd.read_csv("dataset/processed/cleaned_telco.csv")


#     st.subheader("Dataset Preview")
#     st.dataframe(df.head())


#     st.subheader("Churn Distribution")
#     churn_counts = df["churn"].value_counts()
#     st.bar_chart(churn_counts)


# # Display Make Prediction page
#     elif page == "Make Prediction":


#     st.subheader("Enter Customer Details")


#     tenure = st.slider("Tenure (Months)", 0, 72, 12)
#     monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
#     contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])


# # Convert categorical input to numerical encoding
#     input_data = pd.DataFrame({
#         "tenure": [tenure],
#         "monthlycharges": [monthly_charges],
#         # Add other encoded columns as needed
#     })


#     input_scaled = scaler.transform(input_data)


# # Make prediction
#     if st.button("Predict Churn"):


#         prediction = model.predict(input_scaled)
#         probability = model.predict_proba(input_scaled)[0][1]


#         if prediction[0] == 1:
#             st.error(f"⚠️ Customer is likely to churn. Probability: {probability:.2f}")
#         else:
#             st.success(f"✅ Customer is likely to stay. Probability: {probability:.2f}")


# # Run the Streamlit app
# streamlit run app.py
