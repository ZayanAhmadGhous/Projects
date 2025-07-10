import streamlit as st
from PIL import Image

# --- Basic Info ---
st.set_page_config(page_title="Zayan Ahmad Ghous | AI/ML Intern", layout="wide")
st.title("Zayan Ahmad Ghous")
st.subheader("Aspiring AI/ML Engineer | Python Enthusiast")

# --- About Me ---
st.markdown("""
### 👋 About Me
Aspiring Computer Science professional with a strong foundation in programming and a 
passion for Artificial Intelligence. Eager to contribute to innovative projects, solve real-world problems, and gain hands-on experience in a fast-paced AI or software development environment.
""")

# --- Resume Download ---
with open("Zayan_Ahmad_Resume.pdf", "rb") as file:
    btn = st.download_button(
        label="📄 Download Resume",
        data=file,
        file_name="Zayan_Ahmad_Resume.pdf",
        mime="application/pdf"
    )

# --- Skills ---
st.markdown("""
### 🛠️ Skills
- Python (Intermediate)
- Artificial Intelligence (AI)
- Machine Learning (ML)
- Natural Language Processing (NLP)
- Data Cleaning and Preprocessing
- Pandas, NumPy, Scikit-learn
- Matplotlib, Seaborn
- TfidfVectorizer, Label Encoding
- Git & GitHub
- Streamlit
- Jupyter Notebooks
- Consistency
""")

# --- Projects ---
st.markdown("""
### 📁 Projects
""")

projects = [
    ("Titanic Survival Prediction", "https://github.com/ZayanAhmadGhous/Projects/blob/main/01_titanic_ml_project.ipynb"),
    ("Diabetes Detection", "https://github.com/ZayanAhmadGhous/Projects/blob/main/02_diabetes_predeiction.ipynb"),
    ("Heart Disease Prediction", "https://github.com/ZayanAhmadGhous/Projects/blob/main/03_heart_disease_detection.ipynb"),
    ("House Price Prediction (California)", "https://github.com/ZayanAhmadGhous/Projects/blob/main/04_house_price_prediction.ipynb"),
    ("Evaluation Metrics Deep Dive", "https://github.com/ZayanAhmadGhous/Projects/blob/main/05_evaluation_matrix.ipynb"),
    ("Student Performance Prediction", "https://github.com/ZayanAhmadGhous/Projects/blob/main/06_student_performace.ipynb"),
    ("Sentiment Analysis (NLP)", "https://github.com/ZayanAhmadGhous/Projects/blob/main/07_sentiment_analysis.ipynb"),
    ("Titanic Raw EDA Project", "https://github.com/ZayanAhmadGhous/Projects/blob/main/08_titanic_eda.ipynb")
]

for title, link in projects:
    st.markdown(f"- [{title}]({link})")

# --- Links ---
st.markdown("""
### 🔗 Connect With Me
- [GitHub](https://github.com/ZayanAhmadGhous)
- [LinkedIn](https://linkedin.com/in/zayan-ahmad-23863625b)
- zayanahmad.ghous@gmail.com
""")
