from base_app import baseApp
from navigation import Navi
import data_base as data_base
import xml_parser as xml_parser
import os

class page1(baseApp):



    def on_save_to_db_clicked(self,db_name,data):
        data_base.save_test_results_to_db(db_name, data)
        

    def home_page1(self):

        navigation = Navi()
        navigation.make_sidebar()
        self.create_write("# test results! Reporty")
        
        xml = self.create_text_input("Load xml-Results",".xml file path e.g. ../full-path/results/output.xml")
        if xml:
            test_result = xml_parser.TestResult(xml)
            ## Metric
            col1, col2, col3, col4 = self.create_columns(4)
            with col1:
                self.create_metric("Test results","Pass",f"{ test_result.passed }")
            with col2:
                self.create_metric("Test results","Failed",f"{ -test_result.failed }")
            with col3:
                self.create_metric("Test results","Skipped",f"{ test_result.skipped }",delta_color="off")  
            with col4:
                self.create_metric("Test results","Total",f"{ test_result.total }",delta_color="off")

            self.create_dataframe(
                {
                "Test Name": test_result.testsuite_names,
                "Test Case Name": test_result.testcase_names,
                "Status": test_result.testcases_status,
                "Elapsed": test_result.testcases_elapsed
                },
                width=400,
                height=400,
                container_width=True
            )
            if test_result and self.create_button("Save To DB"):


                self.on_save_to_db_clicked("test.db", test_result)
                self.create_toast("Test results saved to database successfully.")
                               

                
        else:
            current_dir = os.getcwd()
            db_files = [file for file in os.listdir(current_dir) if file.endswith(".db")]
            with self.create_spinner("Wait for it..."):
                #time.sleep(1)
                if db_files:
            
                    self.create_dataframe(
                        {
                            "Test Name": data_base.load_db_file("test.db").execute("SELECT test_suite_name FROM test_results").fetchall(),
                            "Test Case Name": data_base.load_db_file("test.db").execute("SELECT test_case_name FROM test_results").fetchall(),
                            "Status": data_base.load_db_file("test.db").execute("SELECT test_case_status FROM test_results").fetchall(),
                            "Elapsed": data_base.load_db_file("test.db").execute("SELECT test_case_elapsed_time FROM test_results").fetchall()
                        },
                        width=400,
                        height=400,
                        container_width=True
                    )
                else:
                    pass

        



if __name__ == "__main__":
    app = page1()
    app.home_page1()

    
