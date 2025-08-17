import requests,mysql.connector

#Extract Data
response=requests.get('https://jsonplaceholder.typicode.com/users')
users=response.json()

# Transform to Mysql Table

new_users = []
for user in users:
    new_users.append((user['id'],
                      user['username'],
                      user['email'],
                      user['address']['city'],
                      user['phone']))

print(new_users)

#Load data into mysql tables
dbcon=None
cursor=None
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='hope')
    cursor=dbcon.cursor()
    sql_statement='''
                  insert into users(uid,uname,email,city,phone) values(%s,%s,%s,%s,%s)
                  '''
    
    cursor.executemany(sql_statement, new_users)
    print(new_users)
    dbcon.commit()  
except mysql.connector.Error as err:
    print(err)
finally:
    dbcon.close()
