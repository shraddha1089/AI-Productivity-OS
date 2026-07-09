import streamlit as st
from  database.database import create_database
# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="AI Productivity OS",
    page_icon="🧠",
    layout="wide"
)

# -------------------------------------------------
# Header
# -------------------------------------------------
st.title("🧠 AI Productivity OS")
st.subheader("Your AI-powered productivity companion")

st.divider()

# -------------------------------------------------
# Hero Section
# -------------------------------------------------
st.markdown("""
## Organize your work.

## Build better habits.

## Automate repetitive tasks.

Welcome to **AI Productivity OS**, a platform designed to help you manage your work, stay focused, and gradually automate your daily productivity using AI.
""")

st.divider()

#create_database()
# -------------------------------------------------
# Footer
# -------------------------------------------------
st.caption("AI Productivity OS • Version 0.1")

