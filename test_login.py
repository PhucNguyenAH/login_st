import streamlit as st
from streamlit_login_auth_ui.widgets import __login__

__login__obj = __login__(auth_token = "Bearer pk_prod_NFP3H2Z1NHMQNTPZG9Y79GMASD01", 
                    company_name = "ycomm",
                    width = 200, height = 250, 
                    logout_button_name = 'Logout', hide_menu_bool = False, 
                    hide_footer_bool = False, 
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:
    st.markdown("Your Streamlit Application Begins here!")


# if LOGGED_IN != True:
#     with open('style2.css') as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)