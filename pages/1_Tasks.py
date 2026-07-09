import streamlit as st
from database.database import create_database, add_task, get_tasks

create_database()
# -------------------------------------------------
# Initialize Session State
# -------------------------------------------------
#if "tasks" not in st.session_state:
#    st.session_state.tasks = []

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

    add_task_button = st.button("➕ Add Task")

    if add_task_button:

        add_task(
            task_name,
            priority,
            str(due_date)
            )

        st.success("Task added successfully!")


# ---------------- Right Column ----------------
tasks = get_tasks()
with col2:

    st.markdown("### 📋 My Tasks")

    if tasks:
        for task in tasks:
            with st.container():
                st.divider()
                st.write("📌",task[1])
                st.write("🔥",task[2])
                st.write("🗓️",task[3])
    else:
        st.info("No tasks added yet. Start by creating your first task!")

st.divider()

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.caption("AI Productivity OS • Version 0.1")