import requests

response=requests.get('https://jsonplaceholder.typicode.com/users')
users=response.json()

# Insert data transformation logic here

new_users = []
for user in users:
    new_users.append((user['id']))

print(new_users)
