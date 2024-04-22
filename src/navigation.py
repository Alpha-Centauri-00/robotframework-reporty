from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages
from base_app import baseApp



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