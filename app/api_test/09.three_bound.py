import requests

# FastAPI 服务的 URL 地址
BASE_URL = "http://localhost:8001"

# 1. 创建用户接口测试
def create_user():
    url = f"{BASE_URL}/users/"
    payload = {
        "username": "testuser",
        "email": "testuser@example.com"
    }
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("Create user successful:", response.json())
    else:
        print("Error creating user:", response.status_code, response.text)

# 2. 查询某个用户的所有视频接口测试
def get_user_videos(user_id):
    url = f"{BASE_URL}/users/{user_id}/videos/"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"User {user_id} videos:", response.json())
    else:
        print(f"Error fetching videos for user {user_id}:", response.status_code, response.text)

# 3. 查询某个用户的某个视频的所有切片接口测试
def get_video_clips(user_id, video_id):
    url = f"{BASE_URL}/users/{user_id}/videos/{video_id}/clips/"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Video {video_id} clips for user {user_id}:", response.json())
    else:
        print(f"Error fetching clips for video {video_id} of user {user_id}:", response.status_code, response.text)

# 4. 查询某个用户的所有视频的所有切片接口测试
def get_user_videos_clips(user_id):
    url = f"{BASE_URL}/users/{user_id}/videos/clips/"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"All clips for user {user_id}:", response.json())
    else:
        print(f"Error fetching all clips for user {user_id}:", response.status_code, response.text)


# 测试流程
def test():
    # 1. 创建用户
    # create_user()
    
    # 假设创建的用户ID为1，测试其他接口
    user_id = 1
    
    # 2. 获取用户的所有视频
    get_user_videos(user_id)
    
    # 假设该用户的第一个视频ID为1，测试获取该视频的所有切片
    video_id = 1
    get_video_clips(user_id, video_id)
    
    # 3. 获取该用户所有视频的所有切片
    get_user_videos_clips(user_id)


if __name__ == "__main__":
    test()


# User 1 videos: [{'file_name': 'example_video.mp4', 'file_path': '/path/to/video.mp4', 'class_name': 'example_class', 'upload_type': 'manual', 'id': 1, 'upload_time': '2025-08-11T08:59:53.492643', 'user_id': 1}, {'file_name': 'example_video3.mp4', 'file_path': '/path/to/video3.mp4', 'class_name': 'example_class', 'upload_type': 'manual', 'id': 2, 'upload_time': '2025-08-11T09:23:22.758906', 'user_id': 1}]
# Video 1 clips for user 1: [{'clip_file_name': 'example_clip.mp4', 'clip_file_path': '/path/to/clip.mp4', 'clip_file_url': 'http://localhost:8000/clip.mp4', 'id': 1, 'video_id': 1}, {'clip_file_name': 'example_clip.mp4', 'clip_file_path': '/path/to/clip1.mp4', 'clip_file_url': 'http://localhost:8000/clip.mp4', 'id': 2, 'video_id': 1}, {'clip_file_name': 'example_clip.mp4', 'clip_file_path': '/path/to/clip2.mp4', 'clip_file_url': 'http://localhost:8000/clip2.mp4', 'id': 3, 'video_id': 1}]
# All clips for user 1: [{'clip_file_name': 'example_clip.mp4', 'clip_file_path': '/path/to/clip.mp4', 'clip_file_url': 'http://localhost:8000/clip.mp4', 'id': 1, 'video_id': 1}, {'clip_file_name': 'example_clip.mp4', 'clip_file_path': '/path/to/clip1.mp4', 'clip_file_url': 'http://localhost:8000/clip.mp4', 'id': 2, 'video_id': 1}, {'clip_file_name': 'example_clip.mp4', 'clip_file_path': '/path/to/clip2.mp4', 'clip_file_url': 'http://localhost:8000/clip2.mp4', 'id': 3, 'video_id': 1}]