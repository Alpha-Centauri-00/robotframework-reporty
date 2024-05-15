import sqlite3

def create_new_db(db_name):
    """
    Create a new SQLite database.
    """
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

            # Create a table to store statistics of test results if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS total_test_results (
                            id INTEGER PRIMARY KEY,
                            passed INTEGER,
                            failed INTEGER,
                            skipped INTEGER,
                            total INTEGER
                        )''')
        
        conn.commit()

        # Create a table to store test results if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS test_results (
                            id INTEGER PRIMARY KEY,
                            test_suite_name TEXT,
                            test_case_name TEXT,
                            test_case_status TEXT,
                            time TEXT,
                            date TEXT,
                            test_case_elapsed_time REAL
                        )''')
        
        conn.commit()
        conn.close()

        print(f"New database '{db_name}' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")  


def load_db_file(db_name):
    """
    Load an existing SQLite database file.

    Args:
        db_name (str): The name of the database file to load.

    Returns:
        sqlite3.Connection: A connection to the loaded database.
    """
    try:
        conn = sqlite3.connect(db_name)
        #print(f"Database '{db_name}' successfully loaded.")
        return conn
    except sqlite3.Error as e:
        print(f"Error loading database: {e}")
        return None
    

def save_test_results_to_db(db_name,data):
    """
    Save test results to the 'test_results' table in the database.

    """
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

            # Create table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS test_results (
                            id INTEGER PRIMARY KEY,
                            test_suite_name TEXT,
                            test_case_name TEXT,
                            test_case_status TEXT,
                            time TEXT,
                            date TEXT,
                            test_case_elapsed_time REAL
                        )''')
        
        # Insert data into the table
        for i in range(len(data.testcase_names)):
            cursor.execute('''INSERT INTO test_results 
                            (test_suite_name, test_case_name, test_case_status, time, date, test_case_elapsed_time) 
                            VALUES (?, ?, ?, ?, ?, ?)''', 
                        (data.testsuite_names[i], data.testcase_names[i], 
                        data.testcases_status[i],data.start_time,data.start_date, data.testcases_elapsed[i]))
            
        cursor.execute('''INSERT INTO total_test_results 
                            (passed, failed, skipped, total) 
                            VALUES (?, ?, ?, ?)''', 
                        (data.passed, data.failed, 
                        data.skipped, data.total))

        conn.commit()

        # Close cursor and connection
        cursor.close()
        conn.close()
        print(f"Test results saved to database '{db_name}' successfully.")
    except sqlite3.Error as e:
        print(f"Error saving test results: {e}")