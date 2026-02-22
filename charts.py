import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# ----------------------------
# 1. Radar Chart (Performance Profile)
# ----------------------------
def plot_radar_chart(marks):

    subjects = list(marks.keys())
    values = list(marks.values())

    values = values + values[:1]
    angles = np.linspace(0, 2*np.pi, len(subjects), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))

    ax.plot(angles, values, linewidth=3)
    ax.fill(angles, values, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(subjects)

    ax.set_title("AI Performance Radar Analysis", fontsize=14)

    st.pyplot(fig)



# ----------------------------
# 2. Strength vs Weakness Chart
# ----------------------------
def plot_strength_weakness(marks):

    subjects = list(marks.keys())
    values = list(marks.values())

    colors = []

    for v in values:
        if v >= 75:
            colors.append("green")
        elif v >= 50:
            colors.append("orange")
        else:
            colors.append("red")

    fig, ax = plt.subplots()

    bars = ax.bar(subjects, values, color=colors)

    ax.set_title("Strength and Weakness Detection")
    ax.set_ylabel("Marks")

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height,
                f'{height}', ha='center', va='bottom')

    st.pyplot(fig)



# ----------------------------
# 3. Performance Distribution Curve
# ----------------------------
def plot_distribution_curve(marks):

    values = list(marks.values())

    fig, ax = plt.subplots()

    ax.hist(values, bins=5, alpha=0.7)

    mean = np.mean(values)

    ax.axvline(mean, linestyle="--")
    ax.set_title("Marks Distribution with Mean Indicator")

    st.pyplot(fig)



# ----------------------------
# 4. AI Performance Score Meter
# ----------------------------
def plot_performance_meter(marks):

    avg = sum(marks.values()) / len(marks)

    fig, ax = plt.subplots()

    ax.barh(["Score"], [avg])

    ax.set_xlim(0, 100)

    ax.set_title("AI Performance Score Meter")

    ax.text(avg - 10, 0, f"{round(avg,2)}", color="white", fontsize=12)

    st.pyplot(fig)



# ----------------------------
# 5. Subject Comparison Line Chart
# ----------------------------
def plot_comparison_line(marks):

    subjects = list(marks.keys())
    values = list(marks.values())

    fig, ax = plt.subplots()

    ax.plot(subjects, values, marker='o', linewidth=3)

    ax.set_title("Subject Performance Trend")

    ax.set_ylabel("Marks")

    ax.grid(True)

    st.pyplot(fig)