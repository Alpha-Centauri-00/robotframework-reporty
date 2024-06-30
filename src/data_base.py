import duckdb

DATABASE_NAME = 'test.duckdb'

def create_sequence(cursor, sequence_name):
    try:
        cursor.execute(f'CREATE SEQUENCE {sequence_name} START 1')
    except Exception as e:
        print(f"Sequence '{sequence_name}' already exists or another error occurred: {e}")
        
def create_new_db(db_name):
    """
    Create a new DuckDB database with necessary tables and sequences.
    """
    try:
        conn = duckdb.connect(db_name)
        cursor = conn.cursor()

        # Create sequences safely
        create_sequence(cursor, 'seq_test_results_id')
        create_sequence(cursor, 'seq_total_test_results_id')

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
    except Exception as e:
        print(f"Error creating database: {e}")
 


def load_db_file(db_name):
    """
    Load an existing DuckDB database file.

    Args:
        db_name (str): The name of the database file to load.

    Returns:
        duckdb.DuckDBPyConnection: A connection to the loaded database.
    """
    try:
        conn = duckdb.connect(db_name)
        return conn
    except Exception as e:
        print(f"Error loading database: {e}")
        return None
    

def save_test_results_to_db(db_name, data):
    """
    Save test results to the 'test_results' table in the database using sequences for ID generation.
    """
    try:
        conn = duckdb.connect(db_name)
        cursor = conn.cursor()

        # Insert data into the test_results table
        for i in range(len(data.testcase_names)):
            cursor.execute('''INSERT INTO test_results 
                            (id, test_suite_name, test_case_name, test_case_status, time, date, test_case_elapsed_time) 
                            VALUES (nextval('seq_test_results_id'), ?, ?, ?, ?, ?, ?)''', 
                        (data.testsuite_names[i], data.testcase_names[i], 
                        data.testcases_status[i], data.start_time[i], data.start_date[i], data.testcases_elapsed[i]))

        # Assuming total_test_results also uses IDs and multiple entries are made
        cursor.execute('''INSERT INTO total_test_results 
                            (id, passed, failed, skipped, total) 
                            VALUES (nextval('seq_total_test_results_id'), ?, ?, ?, ?)''', 
                        (data.passed, data.failed, 
                        data.skipped, data.total))

        conn.commit()

        # Close cursor and connection
        cursor.close()
        conn.close()
        print(f"Test results saved to database '{db_name}' successfully.")
    except Exception as e:
        print(f"Error saving test results: {e}")
