import streamlit as st
import base64

def header_home():

    logo_url="https://i.ibb.co/bRycxvSH/Chat-GPT-Image-Aug-17-2026-07-18-00-PM.png"

    st.markdown(f"""
            <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30">
                    <img src={logo_url} alt="logo" style="height:100px;"/>
                    <h1 style='text-align:center; color:#E0E3FF'>Proxy</h1> 
                    
            </div>
            
        """,unsafe_allow_html=True)

    
def header_dashboard():

    logo_url="https://i.ibb.co/bRycxvSH/Chat-GPT-Image-Aug-17-2026-07-18-00-PM.png"

    st.markdown(f"""
            <div style="display:flex; align-items:left; justify-content:left; gap:10px ">
                    <img src={logo_url} alt="logo" style="height:85px;"/>
                    <h2 style='text-align:left; color:#5865F2'>Proxy</h2> 
                    
            </div>


        """,unsafe_allow_html=True)


