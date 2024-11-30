import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

if "mydict" not in st.session_state:
    st.session_state.mydict = {"To Do":[],"In Progress":[],"Done":[]}

    
def add_task():
    if st.session_state.new_task:
        category = st.session_state.category
        st.session_state.mydict[category].append(st.session_state.new_task)
        st.session_state.new_task = ""

def rem_task():
    if st.session_state.rm_task:
        category = st.session_state.category2
        st.session_state.mydict[category].remove(st.session_state.rm_task)
        
def move_task():
    if st.session_state.mv_task:
        category_f = st.session_state.category3
        category_t = st.session_state.category4
        st.session_state.mydict[category_t].append(st.session_state.mv_task)
        st.session_state.mydict[category_f].remove(st.session_state.mv_task)

def clear_board():
    st.session_state.mydict = {"To Do":[],"In Progress":[],"Done":[]}

c = st.columns([1,1,1,1])
with c[0]:
    exp = st.expander(label="Add", expanded=False)
    with exp:
        st.selectbox("Category:",options=["To Do", "In Progress", "Done"], key="category")
        st.text_input("Task:", placeholder="Enter task here", key="new_task")
        st.button("Add",on_click=add_task)

with c[1]:
    exp = st.expander(label="Remove", expanded=False)
    with exp:
        category = st.selectbox("Category:", options=["To Do", "In Progress", "Done"], key="category2")
        st.selectbox("Task:", options = st.session_state.mydict[category], placeholder="Select task to remove", key="rm_task")
        st.button("Remove",on_click=rem_task)

with c[2]:
    exp = st.expander(label="Move", expanded=False)
    with exp:
        options=["To Do", "In Progress", "Done"]
        category_f = st.selectbox("From:", options=options, key="category3")
        category_t = st.selectbox("To:", options=[opt for opt in options if opt !=category_f], key="category4")
        st.selectbox("Task:", options = st.session_state.mydict[category_f], placeholder="Select task to move", key="mv_task")
        st.button("Move",on_click=move_task)

with c[3]:
    st.button("Clear Board",on_click=clear_board)
    

col1, col2, col3 = st.columns(3)
with col1:
    st.header("To Do", divider=True)

    cont1 = st.container(border=True)
    with cont1:
        for task in st.session_state.mydict["To Do"]:
            st.write(task)

with col2:
    st.header("In Progress", divider=True)
    
    cont2= st.container(border=True)
    with cont2:
        for task in st.session_state.mydict["In Progress"]:
            st.write(task)
    
with col3:
    st.header("Done", divider=True)
    
    cont3= st.container(border=True)
    with cont3:
        for task in st.session_state.mydict["Done"]:
            st.write(task)