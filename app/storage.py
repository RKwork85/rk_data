import alibabacloud_oss_v2 as oss

import os

# 阿里云 OSS 配置信息
ACCESS_KEY_ID = 'YOUR_ACCESS_KEY_ID'
ACCESS_KEY_SECRET = 'YOUR_ACCESS_KEY_SECRET'
ENDPOINT = 'https://oss-cn-your-region.aliyuncs.com'  # OSS的Endpoint, 根据你的Region进行调整
BUCKET_NAME = 'your-bucket-name'

# 创建 OSS 客户端
auth = oss.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
bucket = oss.Bucket(auth, ENDPOINT, BUCKET_NAME)

def upload_video_to_oss(file_path: str, oss_key: str):
    """
    上传视频文件到阿里云 OSS
    """
    try:
        # 上传文件到 OSS
        bucket.put_object_from_file(oss_key, file_path)
        # 生成文件的访问URL
        url = f"https://{BUCKET_NAME}.{ENDPOINT}/{oss_key}"
        return url
    except oss.exceptions.OssError as e:
        print(f"上传失败: {e}")
        return None
