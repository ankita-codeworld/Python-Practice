# write a program to connect to mysql
import mysql.connector

dbcon = None
cursor=None
try:
    dbcon= mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Hope")
    
    cursor=dbcon.cursor()
    sql_statement = "Create table employees(eid int Not Null, ename varchar(32) Not Null, esal float)"
    cursor.execute(sql_statement)
    dbcon.commit()
    print("Table created successfully")

except mysql.connector.Error as err:    # To handle error if any error in try block
    print("Error:", err)

finally:                #it will going to execute always
    if dbcon:
        dbcon.close()