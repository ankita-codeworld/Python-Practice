import mysql.connector
myconn=mysql.connector.connect(host='localhost',
                        user='root',
                        password='root',
                        database='p1')

mycursor=myconn.cursor()
mycursor.execute("SHOW DATABASES")