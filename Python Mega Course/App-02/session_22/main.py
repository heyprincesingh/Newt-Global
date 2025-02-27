import streamlit as st                      #type: ignore
import pandas                               # type: ignore

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Photo.jpg", width=500)

with col2:
    st.title("Prince Singh")
    content = """
Aspiring Software Developer with expertise in Python, Django, Flutter, and API development. Skilled in crafting scalable backend solutions, responsive UIs, and AI-driven applications.
Passionate about delivering efficient, user-centric software with a proven track record of improving system performance and user engagement through impactful projects and internships.
Enthusiastic about leveraging technology to solve real-world problems and drive innovation."""

    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python.
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")