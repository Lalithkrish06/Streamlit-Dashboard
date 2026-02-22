import streamlit as st
import json
import os

# Import AI logic
from models.performance import calculate_weighted_score, predict_improvement

# Import advanced charts
from visualizations.charts import (
    plot_radar_chart,
    plot_strength_weakness,
    plot_distribution_curve,
    plot_performance_meter,
    plot_comparison_line
)

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="Student Performance Shocker",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Student Performance Shocker")
st.write("AI-powered analysis of student academic performance")

# ---------------- LOAD WEIGHTS ----------------
weights_path = "data/weights.json"

if not os.path.exists(weights_path):
    st.error("Error: weights.json not found in data folder")
    st.stop()

with open(weights_path, "r") as file:
    weights = json.load(file)

# ---------------- INPUT SECTION ----------------
st.divider()
st.subheader("Enter Subject Marks")

marks = {}

cols = st.columns(len(weights))

for i, subject in enumerate(weights):
    with cols[i]:
        marks[subject] = st.number_input(
            subject,
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

# ---------------- CORE AI LOGIC ----------------
weighted_score = calculate_weighted_score(marks, weights)

PASS_THRESHOLD = 80
pass_rate = (weighted_score / PASS_THRESHOLD) * 100

# ---------------- RESULTS ----------------
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.success(f"Weighted Score: {weighted_score:.2f}/100")

with col2:
    st.metric("Pass Probability", f"{pass_rate:.1f}%")

# ---------------- AI INSIGHT ----------------
st.subheader("AI Insight")

if weighted_score >= 85:
    st.success("Excellent performance. Student is highly likely to succeed.")

elif weighted_score >= 60:
    st.warning("Moderate performance detected. Improvement recommended.")

else:
    st.error("Low performance detected. Immediate improvement required.")

# ---------------- VISUALIZATION ----------------
st.divider()
st.subheader("AI Performance Analytics")

col1, col2 = st.columns(2)

with col1:
    plot_radar_chart(marks)

with col2:
    plot_strength_weakness(marks)

col3, col4 = st.columns(2)

with col3:
    plot_distribution_curve(marks)

with col4:
    plot_performance_meter(marks)

# ---------------- TREND ANALYSIS ----------------
st.divider()
st.subheader("Subject Performance Trend")

plot_comparison_line(marks)

# ---------------- IMPROVEMENT PREDICTION ----------------
st.divider()
st.subheader("AI Improvement Prediction")

if "Math" in marks:

    improvement = st.slider(
        "Increase Math Marks",
        min_value=0,
        max_value=50,
        value=10
    )

    predicted_score = predict_improvement(
        marks["Math"],
        improvement
    )

    st.metric(
        "Predicted Math Score After Improvement",
        f"{predicted_score}/100"
    )

# ---------------- TOP SUBJECTS ----------------
st.divider()
st.subheader("Top 3 Strongest Subjects")

top_3 = sorted(
    marks.items(),
    key=lambda x: x[1],
    reverse=True
)[:3]

for subject, mark in top_3:
    st.write(f"{subject}: {mark}/100")

# ---------------- WEAK SUBJECTS ----------------
st.divider()
st.subheader("3 Subjects Needing Improvement")

weak_3 = sorted(
    marks.items(),
    key=lambda x: x[1]
)[:3]

for subject, mark in weak_3:
    st.write(f"{subject}: {mark}/100")

# ---------------- FINAL SUMMARY ----------------
st.divider()
st.subheader("Final AI Summary")

st.info(
    f"""
    Overall Score: {weighted_score:.2f}/100  
    Pass Probability: {pass_rate:.1f}%  
    Strongest Subject: {top_3[0][0]}  
    Weakest Subject: {weak_3[0][0]}  
    """
)