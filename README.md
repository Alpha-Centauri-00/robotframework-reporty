# robotframework-reporty
Get more insights from your test results using robotframework-reporty

## Project Ideas

○ **Local Database with SQLite3**: 
- Implement a local database using [SQLite3](https://docs.python.org/3/library/sqlite3.html#) to store test results.

○ **Save Test Result automatically**: 
- Create a listener to automatically save test results while running robot tests

○ **Parsing output.xml**: 
- Leverage the capabilities of `robot.api` to parse the Output.xml file to store the results in a local SQLite3 database.

○ **Dashboard with Streamlit**: 
- Using [Streamlit](https://streamlit.io/) to create a web-based dashboard for visualizing and analyzing test results.

○ **Server Setup**: 
- Implement a command-line interface to easily run a local host server, providing Test results.

○ **Installation Process**: 
- Simplify the setup process with a single `pip install robotframework-reporty` command.

○ **Built-in Database**: 
- Benefit from SQLite3 being a part of Python's standard library, eliminating the need for additional database installations.

# Setup

## Installation

First, clone the repository to your local machine using Git.

Before installing the required packages, it's recommended to set up a virtual environment to isolate your project dependencies. Here's how you can do it:

Open a terminal or command prompt and navigate to your project directory. Then, run the following command to create a virtual environment named `.venv`:

```bash
# On Windows
python -m venv .venv
```

To install the required packages, you can use `pip` with the provided `requirements.txt` file.

```bash
pip install -r requirements.txt
```

Navigate to the `src` directory of the cloned repository in your terminal or command prompt. Then, run the following command to start the application:

```bash
cd src
streamlit run app.py
```