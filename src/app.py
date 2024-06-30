# app.py
from base_app import baseApp
import data_base as db
import os
import time

class App(baseApp):

    def __init__(self):
        super().__init__()
        

    def run(self):

        self.create_title("Welcome to RFW-Reporty!")
        
        self.create_markdown("""
        Reporty is an open-source app built specifically for
        Showing test results, Flipchart, and Analyse.
        
        ### Want to learn more?
        - Check out [Github](#)
        - Jump into our [documentation](#)
        - Ask a question in our [community forums](#)
        """)

        self.create_write("Database Management")

        self.create_header("Database Actions: ")
        
        tab1, tab2, tab3, tab4 = self.create_tabs(["Create DB", "Load DB", "Upload DB","Backup DB"])


        with tab1:
                        
            if self.create_button("Create DB"):
                
                                    
                self.create_toast("New Database successfully created!")

                db.create_new_db("test.duckdb")
                self.create_switch_pages("pages/page1.py")

        with tab2:
            current_dir = os.getcwd()
            db_files = [file for file in os.listdir(current_dir) if file.endswith(".duckdb")]

            if db_files:
                selected_db = self.create_selection("Select Database: ", db_files)
                if self.create_button("Load Selected DB"):

                    self.create_toast("Switching page...")
                    self.create_switch_pages("pages/page1.py")
            

        with tab3:
            self.create_markdown("#### Upload a saved Database (NOT IMPLEMENTED)")

        with tab4:
            self.create_markdown("#### Create a Backup (NOT IMPLEMENTED)")                
        


if __name__ == "__main__":
    app = App()
    app.run()
