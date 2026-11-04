import streamlit as st

st.set_page_config(
    page_title="DevOps CI/CD Demo",
    page_icon="🚀"
)

st.title("🚀 DevOps CI/CD Project")

st.subheader("Welcome to My Application!")

st.write(
    "This application is built using Python and Streamlit."
)

st.success("Application is running successfully!")

st.info("Future deployment: Docker + GitHub Actions")

if st.button("Check Application Status"):
    st.success("Status: Healthy ✅")

st.write("Developed by Tazeen Desai")