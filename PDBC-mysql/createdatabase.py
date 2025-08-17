import mysql.connector
myconn=mysql.connector.connect(host='localhost',
                        user='root',
                        password='root')

mycursor=myconn.cursor()
mycursor.execute("CREATE DATABASE p1")
print("Database created successfully")
