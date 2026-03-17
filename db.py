import mysql.connector

config = {
  "host": "localhost",
  "port": 3306,
  "user": "root",
  "password": "root",
  "database": "digital_hunter"
}


def get_mysql_connection():
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as e:
        print("an error occurred", e)