from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str | None = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes  = True

class VideoBase(BaseModel):
    file_name: str
    file_path: str
    class_name: str | None = None
    upload_type: str = "manual"

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    id: int
    upload_time: datetime
    user_id: int
    
    class Config:
        from_attributes  = True

class VideoClipBase(BaseModel):
    clip_file_name: str
    clip_file_path: str
    clip_file_url: str

class VideoClipCreate(VideoClipBase):
    pass

class VideoClip(VideoClipBase):
    id: int
    video_id: int
    
    class Config:
        from_attributes  = True