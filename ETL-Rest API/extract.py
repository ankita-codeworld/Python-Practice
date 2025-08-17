import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
status_code=response.status_code;
users=response.json()
print(type(users))
print(status_code)
print(response.__dict__)