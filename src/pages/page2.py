from base_app import baseApp
from navigation import Navi

class page2(baseApp):


    def home_page2(self):
        navigation = Navi()
        navigation.make_sidebar()
        self.create_header("Page1 is here 2")


if __name__ == "__main__":
    app = page2()
    app.home_page2()

    
