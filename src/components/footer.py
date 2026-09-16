import streamlit as st


def footer_home():

    logo_url="https://i.ibb.co/nM7J9Tf1/Chat-GPT-Image-Aug-15-2026-08-55-48-PM.png"
    st.markdown(f"""
            <div style="margin-top:2rem; display:flex; gap:5px; justify-content:center; items-align:center">
                <p style="font-weight:bold; color:white;"> Created with ❤️ by</p>
                <img src='{logo_url}' style='max-height:30px'/>
            </div>

                """,unsafe_allow_html=True)

def footer_dashboard():

    logo_url="https://i.ibb.co/nM7J9Tf1/Chat-GPT-Image-Aug-15-2026-08-55-48-PM.png"
    st.markdown(f"""
            <div style="margin-top:2rem; display:flex; gap:5px; justify-content:center; items-align:center">
                <p style="font-weight:bold; color:black;"> Created with ❤️ by</p>
                <img src='{logo_url}' style='max-height:30px'/>
            </div>

                """,unsafe_allow_html=True)
