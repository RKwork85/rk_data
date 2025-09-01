import requests

video_id = 1  # 替换为你实际的视频ID
url = f"http://localhost:8001/videos/{video_id}/clips/"
data = {
    "clip_file_name": "example_clip.mp4",
    "clip_file_path": "/path/to/clip2.mp4",
    "clip_file_url": "http://localhost:8000/clip2.mp4"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Clip created successfully:", response.json())
else:
    print("Error:", response.status_code, response.text)
