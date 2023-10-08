from enum import Enum

import streamlit as st

import util_functions


class ElementKeys(Enum):
    NEW_TODO_INPUT = "NEW_TODO_INPUT",
    TODO_ITEM_PREFIX = "TODO_ITEM_PREFIX",


todos = util_functions.read_todos()


def on_add_new_todo():
    new_todo = st.session_state[ElementKeys.NEW_TODO_INPUT]
    todos.append(new_todo)
    util_functions.save_todos(todos)
    st.session_state[ElementKeys.NEW_TODO_INPUT] = ""
    print(todos)


st.title("Super Awesome TODO App")
st.subheader("This app is to increase your productivity!")
st.write("This is yet another TODO app. Written in Python using the Streamlit framework")

for index, todo in enumerate(todos):
    key = f"{ElementKeys.TODO_ITEM_PREFIX.name}-{index}"
    is_checked = st.checkbox(todo, key=key)
    if is_checked:
        todos.pop(index)
        util_functions.save_todos(todos)
        st.rerun()

st.write("")
st.text_input(key=ElementKeys.NEW_TODO_INPUT, label="New TODO", placeholder="Add a new TODO...",
              on_change=on_add_new_todo)
