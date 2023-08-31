# To load the page without the logo, call the link address with ~/+/ at the end of the URL, 
# example https://ai-assistant-for-doctors.streamlit.app/~/+/

import streamlit
def Release_Mode():
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    streamlit.markdown(hide_st_style, unsafe_allow_html=True)
