# AI Productivity OS - Development Log

---

# Sprint 0 - Day 1 (June 29, 2026)

## Goal
Set up the development environment.

## Completed
- Created GitHub repository
- Installed Git
- Configured Git
- Created Streamlit project
- Successfully pushed first commit

## Learned
- Git init
- Git add
- Git commit
- Git push
- Difference between local and remote repository

## Challenges
- Incorrect GitHub remote URL
- README changes weren't appearing because I forgot to push

## Reflection
Today I understood the complete Git workflow and successfully connected my local project to GitHub.

---

# Sprint 0 - Day 2 (June 30, 2026)

## Goal
Project planning and architecture.

## Completed
- Defined product vision
- Planned Version 1.0 features
- Designed folder structure
- Improved home screen

## Learned
- Product thinking
- Software architecture
- Why planning before coding saves time

## Challenges
(To be filled at the end of today's work)

## Reflection
(To be filled after today's session)

## Next
Build the Dashboard UI.


## Day 3 - Task Manager Comes Alive

### Features Added
- Implemented task creation
- Added session state to persist tasks
- Displayed tasks dynamically using a for loop
- Organized task display using Streamlit containers
- Improved UI with dividers and formatted task cards

### Concepts Learned
- st.session_state
- List of dictionaries
- Dynamic UI rendering
- Python truthy/falsy values
- f-strings
- Streamlit containers

### Key Learning
A Streamlit app reruns from top to bottom on every interaction, so session state is required to preserve data during a user's session.

### Next Goal
- Validate user input
- Prevent empty task names
- Save tasks permanently using SQLite


# Dev Log

## Day 4 – Moving from Temporary Storage to SQLite Database

### Objective

Replace temporary task storage using Streamlit Session State with a permanent SQLite database.

### What I Learned

#### SQLite Fundamentals

* Created my first SQLite database (`tasks.db`).
* Learned that SQLite automatically creates the database file if it doesn't exist.
* Created the `tasks` table using `CREATE TABLE IF NOT EXISTS`.
* Understood the purpose of `PRIMARY KEY AUTOINCREMENT`.

#### Project Architecture

* Separated database logic from the UI by creating a dedicated `database.py` module.
* Learned why application logic and database logic should live in separate files.
* Understood that `app.py` (or the application) should control when functions execute, while helper modules should only define reusable functions.

#### Python Concepts

* Reinforced the difference between **defining** a function and **calling** a function.
* Understood that code inside a function executes only when the function is called.
* Learned how function naming conflicts can create unexpected bugs.

#### Database Operations

Implemented the first two CRUD operations:

* **Create**

  * `create_database()`
  * `add_task()`

* **Read**

  * `get_tasks()`

#### SQL Concepts

Learned and practiced:

* `CREATE TABLE`
* `INSERT INTO`
* `SELECT`
* `VALUES`
* `cursor.execute()`
* `cursor.fetchall()`
* `commit()`
* `close()`

#### Database Security

Learned why SQL queries should use parameterized placeholders (`?`) instead of string concatenation.

Topics explored:

* SQL Injection
* Why user input should never be trusted
* Difference between validation, authentication, and parameterized queries
* Defense in Depth

#### Debugging Experience

Encountered a bug where every task was inserted multiple times.

Root cause:

* Accidentally wrote:

```python
if add_task:
```

instead of

```python
if add_task_button:
```

Since `add_task` is a function, Python treated it as a truthy object, causing the insertion logic to execute on every Streamlit rerun.

Resolved by checking the correct button variable.

### Current Project Status

✅ Multi-page Streamlit application

✅ SQLite database integrated

✅ Permanent task storage

✅ Database-driven task display

✅ Clean separation between UI and database logic

### Reflection

Today's work marked the transition from a simple prototype to a database-driven application.

More importantly, I learned how data flows from the user interface to the database and back to the application, along with the importance of software architecture, reusable functions, and secure database programming.
