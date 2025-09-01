import requests
user_id = 1  # 替换为你实际的用户ID
url = f"http://localhost:8001/users/{user_id}/videos/"
data = {
    "file_name": "example_video3.mp4",
    "file_path": "/path/to/video3.mp4",
    "class_name": "example_class",
    "upload_type": "manual"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Video created successfully:", response.json())
else:
    print("Error:", response.status_code, response.text)
