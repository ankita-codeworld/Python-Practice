#WAP to create connection to mysql

import mysql.connector

myconn=mysql.connector.connect(host='localhost',        #created object myconn
						user='root',
						password='root')
print(myconn)                                           # Calling object to get to know connection established or no
