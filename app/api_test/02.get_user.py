import requests
user_id = 1  # 替换为你实际的用户ID
url = f"http://localhost:8001/users/{user_id}"

response = requests.get(url)

if response.status_code == 200:
    print("User info:", response.json())
else:
    print("Error:", response.status_code, response.text)
