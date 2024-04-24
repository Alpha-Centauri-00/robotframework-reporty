# robotframework-reporty
Get more insights from your test results using robotframework-reporty

> Disclaimer: This library is currently in early development and is intended for testing and experimentation purposes only. It is not recommended for use in production environments. Please use at your own risk. Feedback and issue reports are highly appreciated as we continue to improve the library. Thank you for your understanding.⚠️

## Project Ideas

**Local Database with SQLite3**: 
- Implement a local database using [SQLite3](https://docs.python.org/3/library/sqlite3.html#) to store test results.

**Save Test Result automatically**: 
- Create a listener to automatically save test results while running robot tests (NOT IMPLEMENTED YET)

**Parsing output.xml**: 
- Leverage the capabilities of `robot.api` to parse the Output.xml file to store the results in a local SQLite3 database.

**Dashboard with Streamlit**: 
- Using [Streamlit](https://streamlit.io/) to create a web-based dashboard for visualizing and analyzing test results.

**Server Setup**: 
- Implement a command-line interface to easily run a local host server, providing Test results.

**Installation Process**: 
- Simplify the setup process with a single `pip install robotframework-reporty` command.(NOT IMPLEMENTED YET)

**Built-in Database**: 
- Benefit from SQLite3 being a part of Python's standard library, eliminating the need for additional database installations.

**Cross-Platform**:
- Ensure that `robotframework-reporty` works seamlessly on different operating systems such as Windows, macOS, and Linux.

## Installation

First, clone the repository to your local machine using Git.

Before installing the required packages, it's recommended to set up a virtual environment to isolate your project dependencies. Here's how you can do it:

Open a terminal or command prompt and navigate to your project directory. Then, run the following command to create a virtual environment named `.venv`:

```bash
# On macOS/Linux
python3 -m venv .venv

# On Windows
python -m venv .venv

```
Activate the virtual environment:

```bash
# On macOS/Linux
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
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

# Enjoy!

## Recommendations

### Visual Studio Code and SQLite3 Editor Extension

To work with SQLite databases seamlessly in VS Code, we suggest installing the "SQLite3 Editor" extension. This extension provides a convenient interface for browsing, querying, and managing SQLite databases directly within VS Code.

## Having Trouble?

If you encounter any issues, have questions, or want to suggest improvements, please feel free to [create a new issue](https://github.com/Alpha-Centauri-00/robotframework-reporty/issues) on GitHub. 

When creating an issue, be sure to provide detailed information about the problem you're experiencing, including steps to reproduce it if possible. This will help us understand and resolve the issue more efficiently.

We appreciate your feedback to making this project better!

