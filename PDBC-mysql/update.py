import mysql.connector

dbcon=None
cursor= None
try:
    dbcon=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='Hope')
    
    cursor=dbcon.cursor()
    sql_statement='''insert into employees
                    values(101,'Rahul', 4500.45);
                    '''
    cursor.execute(sql_statement)
    dbcon.commit()
    print("Record inserted successfully:")

except mysql.connector.Error as err:
    print("Error occured:",err)
finally:
    dbcon.close()