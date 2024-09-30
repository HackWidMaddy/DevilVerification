import streamlit as st
import requests

# Streamlit input fields
website_name = st.text_input("Website Name:")
redirect_to = st.text_input("Redirect To:")
payload = st.text_area("Payload:")

if st.button("Create Slog"):
    response = requests.post("http://127.0.0.1:5000/create_slog", json={
        'website_name': website_name,
        'redirect_to': redirect_to,
        'payload': payload
    })

    if response.status_code == 200:
        slog_link = response.json().get('slog_link')
        st.success(f"Slog created: {slog_link}")
    else:
        st.error("Failed to create slog.")
