import mysql.connector
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ajay@1906",
        database="attendance_db"
    )
    return connection
