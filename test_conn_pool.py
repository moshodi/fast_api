import mysql.connector.pooling

query = str(input("enter query : "))

dbconfig = {
    "host": "rankidb.c39jpvgy5agc.us-east-2.rds.amazonaws.com",
    "user": "admin",
    "password": "Phxntom10$!",
    "database": "rankidb"
}
connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_size=1, **dbconfig)
connection = connection_pool.get_connection()
connection.c