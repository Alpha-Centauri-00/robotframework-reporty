
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

def create_header():

    

    # selected3 = option_menu(None, ["Home", "Analytics",  "Tasks", 'Settings'], 
    #     icons=['house', 'graph-up-arrow', "list-task", 'gear'], 
    #     menu_icon="cast", default_index=0, orientation="horizontal",
    #     styles={
    #         "container": {"padding": "0!important", "background-color": "#009a91"},
    #         "icon": {"color": "#46fff4", "font-size": "25px"}, 
    #         "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#aaa"},
    #         "nav-link-selected": {"background-color": "#009a91"},
    #     }
    # )
    # selected3

    st.markdown(
        
        r"""
        <style>
        .stDeployButton {
                visibility: hidden;
            }
        #MainMenu {visibility: hidden;}

        </style>
        """, unsafe_allow_html=True
    )



    #st.header('This is a header with a divider', divider='rainbow')
    st.header('Reporty is :blue[cool] :sunglasses:')
    

    # 1. as sidebar menu
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home","Analytics", 'Settings'], 
            icons=['house','graph-up-arrow', 'gear'], menu_icon="cast", default_index=1,
            styles={
                "container": {"padding": "0!important", "background-color": "#009a91"},
                "icon": {"color": "#46fff4", "font-size": "25px"}, 
                "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#aaa"},
                "nav-link-selected": {"background-color": "#009a91"},
            })
            
    selected


    
    




# def navigation_bar():
#     import streamlit as st

# 1. as sidebar menu
    # with st.sidebar:
    #     selected = option_menu("Main Menu", ["Home", 'Settings'], 
    #         icons=['house', 'gear'], menu_icon="cast", default_index=1)
    #     selected

    # # 2. horizontal menu
    # selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    #     icons=['house', 'cloud-upload', "list-task", 'gear'], 
    #     menu_icon="cast", default_index=0, orientation="horizontal")
    # selected2

    # 3. CSS style definitions

    # # 4. Manual item selection
    # if st.session_state.get('switch_button', False):
    #     st.session_state['menu_option'] = (st.session_state.get('menu_option', 0) + 1) % 4
    #     manual_select = st.session_state['menu_option']
    # else:
    #     manual_select = None
        
    # selected4 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    #     icons=['house', 'cloud-upload', "list-task", 'gear'], 
    #     orientation="horizontal", manual_select=manual_select, key='menu_4')
    # st.button(f"Move to Next {st.session_state.get('menu_option', 1)}", key='switch_button')
    # selected4

    # # 5. Add on_change callback
    # def on_change(key):
    #     selection = st.session_state[key]
    #     st.write(f"Selection changed to {selection}")
        
    # selected5 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'],
    #                         icons=['house', 'cloud-upload', "list-task", 'gear'],
    #                         on_change=on_change, key='menu_5', orientation="horizontal")
    # selected5