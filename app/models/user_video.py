from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base  # ✅ 使用独立的 Base

class User(Base):
    """用户数据模型"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)  # 唯一用户名
    email = Column(String(100), unique=True)  # 可选邮箱
    created_at = Column(DateTime, default=datetime.utcnow)  # 创建时间
    
    # 一对多关系：一个用户对应多个视频
    videos = relationship("Video", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"


class Video(Base):
    """原始视频数据模型"""
    __tablename__ = 'videos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String(100), nullable=False)  # 原始文件名
    file_path = Column(String(255), nullable=False)  # 存储路径
    class_name = Column(String(50))  # 分类名称（可选）
    upload_type = Column(String(20), default="manual")  # 上传类型
    upload_time = Column(DateTime, default=datetime.utcnow)  # 上传时间
    
    # 外键关联用户
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    
    # 关系
    user = relationship("User", back_populates="videos")  
    clips = relationship("VideoClip", back_populates="video", cascade="all, delete-orphan")  

    def __repr__(self):
        return f"<Video(id={self.id}, file_name='{self.file_name}', file_path='{self.file_path}')>"


class VideoClip(Base):
    """切片视频数据模型"""
    __tablename__ = 'video_clips'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    clip_file_name = Column(String(100), nullable=False)  # 切片文件名
    clip_file_path = Column(String(255), nullable=False)  # 切片存储路径
    clip_file_url = Column(String(255), nullable=False)  # 切片访问URL
    
    # 外键关联原始视频
    video_id = Column(Integer, ForeignKey('videos.id', ondelete="CASCADE"), nullable=False)
    
    # 关系
    video = relationship("Video", back_populates="clips")  

    def __repr__(self):
        return f"<VideoClip(id={self.id}, clip_file_name='{self.clip_file_name}', clip_file_url='{self.clip_file_url}')>"
