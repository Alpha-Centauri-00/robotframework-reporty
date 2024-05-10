# base_app.py
import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages


class baseApp:

    
    def create_title(self,title):
        return st.title(title)
    
    @staticmethod
    def create_sidebar():
        return st.sidebar

    def create_write(self, content):
        return st.write(content)

    def create_markdown(self,content):
        return st.markdown(content)

    def create_header(self,content):
        return st.header(content)
    
    def create_text_input(self,content,placeholder=""):
        return st.text_input(label=content,placeholder=placeholder)
    
    def create_button(self,content,key=None):
        return st.button(content,key)
    
    def create_tabs(self,content):
        return st.tabs(content)
    
    def create_toast(self,content):
        return st.toast(content)
    
    def create_spinner(self,content):
        return st.spinner(content)

    def create_switch_pages(self,content):
        return st.switch_page(content)
    
    def create_warning(self,content):
        return st.warning(content)
    
    def create_selection(self,label,content):
        return st.selectbox(label,content)

    def create_page_link(self,page,label):
        return st.page_link(page=page,label=label)

    def create_file_uploader(self,label,type):
        return st.file_uploader(label,type)
    
    def create_metric(self,label,values,delta,delta_color = "normal"):
        return st.metric(label,values,delta,delta_color)
    
    def create_dataframe(self,data,width,height,container_width):
        return st.dataframe(data,width=width,height=height,use_container_width=container_width)
    
    def create_success(self,message):
        return st.success(message)
        
    def create_columns(self, num_columns):
        return st.columns(num_columns)
    
    @st.experimental_dialog("Save to Database")
    def save_to_the_database(self,callable, *args, **kwargs):
        st.write("Are you sure you want to save to the database?")
        yes_clicked = st.button("Yes")
        no_clicked = st.button("No")

        if yes_clicked:
            callable(*args, **kwargs)
            st.rerun()
        if no_clicked:
            st.rerun()
    
    def create_rerun(self):
        return st.rerun()
    
    def create_date_input(self, label, value):
        return st.date_input(label, value)
    
    def create_session_state(self):
        return st.session_state
    
    def get_session_state(self,val,key):
        return st.session_state.get(val,key)
    

class Navi(baseApp):

    def __init__(self):
        super().__init__()

    def get_current_page_name():
        ctx = get_script_run_ctx()
        if ctx is None:
            raise RuntimeError("Couldn't get script context")

        pages = get_pages("")
        return pages[ctx.page_script_hash]["page_name"]


    def make_sidebar(self):
        with self.create_sidebar():

            self.create_title(title="RFW-Reporty")
            self.create_write("")
            self.create_write("")

            
            self.create_page_link(page="pages/page1.py", label="Test Results")
            self.create_page_link(page="pages/page2.py", label="Test Analyse")


            self.create_write("")
            self.create_write("")

            if self.create_button("Back"):
                self.go_back()

    def go_back(self):
        self.create_switch_pages("app.py")