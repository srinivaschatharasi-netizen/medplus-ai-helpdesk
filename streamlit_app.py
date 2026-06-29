import streamlit as st

st.set_page_config(
    page_title="MedPlus AI Helpdesk",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 MedPlus AI Helpdesk")

st.markdown("### Welcome to MedPlus IT Support")

issue = st.selectbox(
    "Select your issue",
    [
        "Internet",
        "POS",
        "Printer",
        "Monitor",
        "Telephone",
        "Barcode Scanner",
        "Biometric",
        "CCTV",
        "TV"
    ]
)

st.write("Selected Issue:", issue)

if st.button("Start Troubleshooting"):
    st.success(f"Starting troubleshooting for {issue}...")
