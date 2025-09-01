import requests
video_id = 1  # 替换为你实际的视频ID
url = f"http://localhost:8001/videos/{video_id}"

response = requests.get(url)

if response.status_code == 200:
    print("Video info:", response.json())
else:
    print("Error:", response.status_code, response.text)
