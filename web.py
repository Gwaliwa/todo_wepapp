from sys import exception

import streamlit as st
from streamlit import session_state

import functions
from functions import readfile, writefile

todos = readfile()

def add_todo():
    todo=st.session_state["new_todo"]
    todos.append(todo + "\n")
    writefile(todos)
    print(todo)
    exception()

st.title("My Todo App")
st.subheader("my todo list")
st.write("This app will increase your efficiency")

for index, itemdo in enumerate(todos):
    checkbox = st.checkbox(itemdo, key=itemdo)
    if checkbox:
        todos.pop(index)
        writefile(todos)
        del session_state[itemdo]
        st.rerun()


st.text_input(label= "Enter to do here: ", placeholder= "add to do", on_change=add_todo, key="new_todo")