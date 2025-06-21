import streamlit as st
import functions as f

todos = f.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    # session state is used to store the value of the input field
    todos = f.get_todos()
    todos.append(new_todo)
    f.write_todos(todos)
    st.session_state["new_todo"] = ""  # Clear the input field after adding

st.title("To-Do App")
st.subheader("Manage your tasks efficiently")
st.write("This is a simple To-Do application built with Streamlit.")
st.write("You can add, edit, and delete tasks.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ", placeholder="Add a new task", key="new_todo"
              , on_change = add_todo)