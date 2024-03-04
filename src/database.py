import sqlite3

def create_database():
    conn = sqlite3.connect('robot.db')

    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS tests 
                (id INTEGER PRIMARY KEY,
                name TEXT,
                result TEXT)""")

    example_data = [
        ('Test 1', 'Pass'),
        ('Test 2', 'Fail'),
        ('Test 3', 'Pass'),
        ('Test 4', 'Pass'),
        ('Test 5', 'Skip')
    ]

    cursor.executemany("""INSERT INTO tests(name, result) VALUES (?,?)""", example_data)
    conn.commit()
    conn.close()

    print("Database created!")


def select_all_tests():
    conn = sqlite3.connect(r'D:\robotframework-reporty\robot.db')
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tests")
    results = cursor.fetchall()
    for result in results:
        print(result)
    conn.close()

#create_database()
#select_all_tests()