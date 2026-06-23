import streamlit as st
import joblib

model = joblib.load("placement_model.pkl")
with st.sidebar:
    st.header("📋 Project Information")

    st.write("🎓 Project: Placement Prediction")
    st.write("🏫 Department: ECE")
    st.write("🏛 University: Sathyabama University")
    st.write("👨‍💻 Developed By: Hari")

    st.markdown("---")

    st.info("Machine Learning Based Prediction System")
st.set_page_config(
    page_title="Placement Prediction System",
    page_icon="🎓",
    layout="wide"
)
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(to right, #0f0c29, #302b63, #24243e);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #121212;
}

/* All Text */
h1, h2, h3, h4, h5, h6, p, label {
    color: white !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(to right, #8e2de2, #4a00e0);
    color: white;
    font-size: 20px;
    border-radius: 12px;
    height: 55px;
    width: 100%;
    border: none;
    font-weight: bold;
}

/* Metric Box */
[data-testid="stMetric"] {
    background-color: rgba(255,255,255,0.1);
    padding: 15px;
    border-radius: 12px;
}

/* Number Input Boxes */
.stNumberInput {
    background-color: rgba(255,255,255,0.05);
    border-radius: 10px;
    padding: 5px;
}

</style>
""", unsafe_allow_html=True)



st.markdown("""
<h1 style='text-align:center; color:#c77dff;'>
🎓 Student Placement Prediction System
</h1>

<h4 style='text-align:center; color:white;'>
AI Powered Placement Prediction using Machine Learning
</h4>
""", unsafe_allow_html=True)

st.markdown("---")
st.success("✅ Model Accuracy: 96.25%")

st.info("Enter student details below and click Predict.")

col1, col2 = st.columns(2)

with col1:
    cgpa = st.number_input("CGPA", 0.0, 10.0, 6.0)
    attendance = st.number_input("Attendance (%)", 0, 100, 70)
    aptitude = st.number_input("Aptitude Score", 0, 100, 60)
    communication = st.number_input("Communication", 0, 100, 60)

with col2:
    coding = st.number_input("Coding Skill", 0, 100, 60)
    projects = st.number_input("Projects", 0, 10, 2)
    internship = st.number_input("Internship (0/1)", 0, 1, 0)
    mock = st.number_input("Mock Interview", 0, 100, 60)
predict_btn = st.button("🚀 Predict Placement")
if predict_btn:
    student = [[
        cgpa,
        attendance,
        aptitude,
        communication,
        coding,
        projects,
        internship,
        mock
    ]]

    result = model.predict(student)
    prob = model.predict_proba(student)
    percentage = prob[0][1] * 100
    
    if result[0] == "Placed":
     st.success("🎉 Student is likely to be Placed")
    else:
     st.error("❌ Student is likely to be Not Placed")

    st.markdown("### 📊 Prediction Result")

    st.metric(
      label="Placement Probability",
      value=f"{percentage:.2f}%"
)
    st.progress(int(percentage))
    if percentage >= 80:
     risk = "Low Risk"
    elif percentage >= 50:
     risk = "Medium Risk"
    else:
     risk = "High Risk"
    st.write("Risk Level:", risk)

   
st.markdown("---")
st.caption("Placement Prediction System | Developed by Hari | 2026")