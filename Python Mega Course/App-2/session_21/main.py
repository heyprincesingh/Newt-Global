import streamlit as st

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
