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