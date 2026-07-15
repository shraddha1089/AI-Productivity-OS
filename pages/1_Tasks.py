import streamlit as st

from database.database import (
    create_database,
    add_task,
    get_tasks,
    delete_task
)

create_database()

if "delete_task_id" not in st.session_state:
    st.session_state.delete_task_id = None

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
                
                col_1, col_2 =st.columns(2)
                
                with col_1:
                    edit_task_button = st.button("Edit", key=f"edit_{task[0]}")

                with col_2:
                    
                    delete_task_button = st.button("Delete", key=f"delete_{task[0]}")
                    
                    if delete_task_button:
                        st.session_state.delete_task_id = task[0]
                        
                    if st.session_state.delete_task_id == task[0]:
                        st.warning("Are you sure you want to delete this task?")
                        col_11, col_22 = st.columns(2)

                        with col_11:
                            yes_button = st.button("YES", key=f"YES_{task[0]}")
                                
                            if yes_button:
                                delete_task(st.session_state.delete_task_id)
                                st.session_state.delete_task_id = None
                                st.rerun()

                        with col_22:
                            cancel_button =st.button("Cancel", key=f"Cancel_{task[0]}")
                            if cancel_button:
                                st.session_state.delete_task_id = None
                                    
    else:
        st.info("No tasks added yet. Start by creating your first task!")

st.divider()

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.caption("AI Productivity OS • Version 0.1")