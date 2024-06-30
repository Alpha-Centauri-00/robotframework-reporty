from base_app import baseApp, Navi
import data_base as data_base
import xml_parser as xml_parser
from robot.errors import DataError
import os

class page1(baseApp):
    def on_save_to_db_clicked(self, db_name, data):
        data_base.save_test_results_to_db(db_name, data)

    def fetch_data(self, db_name):
        conn = data_base.load_db_file(db_name)
        if conn is not None:
            try:
                cursor = conn.cursor()
                results = {
                    "Test Name": cursor.execute("SELECT test_suite_name FROM test_results").fetchall(),
                    "Test Case Name": cursor.execute("SELECT test_case_name FROM test_results").fetchall(),
                    "Status": cursor.execute("SELECT test_case_status FROM test_results").fetchall(),
                    "Date": cursor.execute("SELECT date FROM test_results").fetchall(),
                    "Time": cursor.execute("SELECT time FROM test_results").fetchall(),
                    "Elapsed": cursor.execute("SELECT test_case_elapsed_time FROM test_results").fetchall()
                }
                cursor.close()
                return results
            except Exception as e:
                print(f"An error occurred while fetching data: {e}")
                self.create_warning(f"An error occurred: {e} ⚠️")
            finally:
                conn.close()
        else:
            self.create_warning("Failed to connect to the database ⚠️")
            print("Failed to connect to the database.")
        return None

    def home_page1(self):
        navigation = Navi()
        navigation.make_sidebar()
        self.create_write("# test results! Reporty")

        xml = self.create_text_input("Load xml-Results", ".xml file path e.g. ../full-path/results/output.xml")
        try:

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
                    "Date": test_result.start_date,
                    "Time": test_result.start_time,
                    "Elapsed": test_result.testcases_elapsed
                    },
                    width=400,
                    height=400,
                    container_width=True
                )
                if test_result and self.create_button("Save To DB"):
                    self.save_to_the_database(lambda: self.on_save_to_db_clicked(data_base.DATABASE_NAME, test_result))
                # Display parsed XML data here as previously outlined...

            else:
                # Assume you want to fetch data if XML isn't provided
                current_dir = os.getcwd()
                db_files = [file for file in os.listdir(current_dir) if file.endswith(".duckdb")]
                if db_files:
                    with self.create_spinner("Loading data..."):
                        results = self.fetch_data(data_base.DATABASE_NAME)
                        if results:
                            self.create_dataframe(results, width=400, height=400, container_width=True)
                else:
                    self.create_warning("No database files found in the current directory ⚠️")
        except DataError as e:
            self.create_warning(f"Error parsing XML: {e} ⚠️")



if __name__ == "__main__":
    app = page1()
    app.home_page1()

    
