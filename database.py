#import sqlite3
import sqlite3

# Create table
CREATE_BEANS_TABLE = "CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);"

#Add beans to the database using users input
INSERT_BEAN = "INSERT INTO beans (name, method, rating) VALUES (?,?,?);"

# Query to get/find a bean
GET_ALL_BEANS = "SELECT * FROM beans;"

# Query to get the bean by name
GET_BEANS_BY_NAME = "SELECT * FROM beans WHERE name = ?;"

# Query to get the  best method for a specific bean 
GET_BEST_PREPARATION_FOR_BEAN = """ 
SELECT * FROM beans
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""



# Create a conect function and create  our database
def connect():
    return sqlite3.connect("project.db")

# Execute our query to create our table
def create_tables(connection):
    with connection:
        connection.execute(CREATE_BEANS_TABLE)

# Functions to Add beans to the database using users input
def add_bean(connection, name, method, rating):
    with connection:
        connection.execute(INSERT_BEAN, (name, method, rating))

# Function to get/find a bean
def get_all_beans(connection):
    with connection:
        connection.execute(GET_ALL_BEANS).fetchall()

# Function to find/get the bean by name
def get_beans_by_name(connection, name):
    with connection:
        connection.execute(GET_BEANS_BY_NAME, (name,)).fetchall()

# Function to get the  best method for a specific bean 
def get_best_preparation_for_bean(connection, name):
    with connection:
        connection.execute(GET_BEST_PREPARATION_FOR_BEAN, (name,)).fetchone()