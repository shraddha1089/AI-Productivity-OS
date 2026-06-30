import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Productivity OS",
    page_icon="🧠",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("🧠 AI Productivity OS")

st.subheader("Your AI-powered productivity companion")

st.divider()

# -----------------------------
# Hero Section
# -----------------------------
st.markdown("""
### Organize your work.

### Build better habits.

### Automate repetitive tasks.

Welcome to **AI Productivity OS**, a platform that will help you manage your work, understand your productivity, and use AI to stay focused.
""")

#st.write("")

# -----------------------------
# Call to Action
# -----------------------------
if st.button("🚀 Get Started"):
    st.success("Welcome! We'll begin by setting up your first tasks in the next version.")

st.divider()

# -----------------------------
# Upcoming Features
# -----------------------------
st.subheader("🚀 Roadmap")

st.markdown("""
- ✅ Smart Task Management
- 🤖 AI Productivity Coach *(Coming Soon)*
- 📊 Analytics Dashboard *(Coming Soon)*
- 📅 Calendar Integration *(Coming Soon)*
- ⚡ Workflow Automation *(Coming Soon)*
""")

st.divider()

st.caption("Version 0.1 • Built with Python + Streamlit")