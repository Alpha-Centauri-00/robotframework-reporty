from base_app import baseApp, Navi
import datetime

class page2(baseApp):


    def home_page2(self):
        navigation = Navi()
        navigation.make_sidebar()
        self.create_header("Page2 is here!")

        self.create_markdown("####  Show test results by date range")

        col1, col2 = self.create_columns(2)
        with col1:
            self.create_date_input("From: ",datetime.date(2024, 1, 1))

        with col2:
            self.create_date_input("To: ",datetime.date(2024, 1, 1))

        self.create_write("Not Implemented yet..")

if __name__ == "__main__":
    app = page2()
    app.home_page2()

    
