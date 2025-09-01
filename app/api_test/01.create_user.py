import requests

url = "http://localhost:8001/users/"
data = {
    "username": "john_doee",
    "email": "johdoe@example.com"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("User created successfully:", response.json())
else:
    print("Error:", response.status_code, response.text)
