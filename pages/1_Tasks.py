import streamlit as st
# -------------------------------------------------
# Task Manager
# -------------------------------------------------
st.title("📝 Task manager")

st.markdown("""
Manage your daily tasks efficiently.

Add a task on the left and track it on the right.
""")

st.divider()

col1, col2 = st.columns(2)

# ---------------- Left Column ----------------
with col1:

    st.markdown("### ➕ Add New Task")

    task_name = st.text_input("Task Name")

    priority = st.selectbox(
        "Priority",
        ["High", "Medium", "Low"]
    )

    due_date = st.date_input("Due Date")

    add_task = st.button("➕ Add Task")

# ---------------- Right Column ----------------
with col2:

    st.markdown("### 📋 My Tasks")

    st.info("No tasks added yet. Start by creating your first task!")

st.divider()

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.caption("AI Productivity OS • Version 0.1")