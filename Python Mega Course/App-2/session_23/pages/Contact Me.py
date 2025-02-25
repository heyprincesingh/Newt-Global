import streamlit as st                      #type: ignore
from send_email import send_email

st.header("Contact Me")

with st.form(key="email-form"):
    user_email = st.text_input("Your email address")
    option = st.selectbox("Subject", ("General Inquiry", "Job Opportunity", "Other"))
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")

    message = f"""\
Subject: {option}

{message}
"""

    if button:
        send_email(user_email=user_email, message=message)
        st.info("Your email was sent successfully!")