import mysql.connector
myconn=mysql.connector.connect(host='localhost',
                        user='root',
                        password='root',
                        database='p1')
mycursor=myconn.cursor()
sql_statement= '''uid=101, uname='Rahul' '''
mycursor.execute(sql_statement)
