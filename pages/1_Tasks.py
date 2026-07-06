from asyncio import tasks

import streamlit as st

# -------------------------------------------------
# Initialize Session State
# -------------------------------------------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

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

    if add_task:

        task = {
            "task_name": task_name,
            "priority": priority,
            "due_date": due_date
                }

        st.session_state.tasks.append(task)
    

# ---------------- Right Column ----------------
with col2:

    st.markdown("### 📋 My Tasks")

    if st.session_state.tasks:
        for task in st.session_state.tasks:
            with st.container():
                st.markdown("----------------------------------------------------")
                st.write("📌", task["task_name"])
                st.write("🔥",task["priority"])
                st.write("🗓️",task["due_date"])
    else:
        st.info("No tasks added yet. Start by creating your first task!")

st.divider()

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.caption("AI Productivity OS • Version 0.1")