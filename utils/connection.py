import mysql.connector
def connection(database = None):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password='12345',
        database = database
        )
    
    cur = conn.cursor()

    return cur,conn

cur,conn = connection(database=None)
