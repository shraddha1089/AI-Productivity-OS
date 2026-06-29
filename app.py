import streamlit as st

st.set_page_config(
    page_title="AI Productivity Assistant",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Productivity Assistant")

st.write("Welcome! Let's organize your day.")

st.divider()

task = st.text_input("Enter your task")

category = st.selectbox(
    "Category",
    [
        "Work",
        "Learning",
        "Health",
        "Personal"
    ]
)

priority = st.selectbox(
    "Priority",
    [
        "High",
        "Medium",
        "Low"
    ]
)

if st.button("Add Task"):
    st.success("Task added successfully!")