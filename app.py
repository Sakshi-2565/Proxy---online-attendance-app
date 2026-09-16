import streamlit as st
import pandas as pd
from src.components.auto_enroll_dialog import auto_enroll_dialog
from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen
from PIL import Image

def main():
    st.set_page_config(
        page_title='Proxy - Student Attendance.Simplified!',
        page_icon= r"src\img\ChatGPT Image Jun 24, 2026, 07_13_28 PM.png"
    )
    
    if 'login_type' not in st.session_state:
        st.session_state.login_type = None

    match st.session_state.login_type:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
            
        case None:
            home_screen()

    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)


main()