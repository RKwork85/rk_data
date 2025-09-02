"""
* @Description: V1 版本 - 用户 & 视频 & 切片接口
* @Author: rkwork
* @Date: 2025-09-02
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.database import get_db
from app.models import user_video

router = APIRouter(prefix="/v1", tags=["🎬 视频处理"])

# =====================
# 用户接口
# =====================

@router.post("/users/", response_model=schemas.User, summary="创建用户")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(user_video.User).filter(user_video.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    new_user = user_video.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users/count/", response_model=int, summary="查询用户数量")
def get_user_count(db: Session = Depends(get_db)):
    return db.query(user_video.User).count()


@router.get("/users/{user_id}", response_model=schemas.User, summary="查询用户信息")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(user_video.User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# =====================
# 视频接口
# =====================

@router.post("/users/{user_id}/videos/", response_model=schemas.Video, summary="用户上传视频")
def create_video(user_id: int, video: schemas.VideoCreate, db: Session = Depends(get_db)):
    user = db.query(user_video.User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_video = user_video.Video(**video.dict(), user_id=user_id)
    db.add(new_video)
    db.commit()
    db.refresh(new_video)
    return new_video


@router.get("/videos/{video_id}", response_model=schemas.Video, summary="查询视频详情")
def read_video(video_id: int, db: Session = Depends(get_db)):
    video = db.query(user_video.Video).get(video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video


@router.get("/users/{user_id}/videos/", response_model=list[schemas.Video], summary="查询用户的所有视频")
def read_user_videos(user_id: int, db: Session = Depends(get_db)):
    user = db.query(user_video.User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.videos


# =====================
# 切片接口
# =====================

@router.post("/videos/{video_id}/clips/", response_model=schemas.VideoClip, summary="为视频添加切片")
def create_clip(video_id: int, clip: schemas.VideoClipCreate, db: Session = Depends(get_db)):
    video = db.query(user_video.Video).get(video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    new_clip = user_video.VideoClip(**clip.dict(), video_id=video_id)
    db.add(new_clip)
    db.commit()
    db.refresh(new_clip)
    return new_clip


@router.get("/videos/{video_id}/clips/", response_model=list[schemas.VideoClip], summary="查询视频的所有切片")
def read_clips(video_id: int, db: Session = Depends(get_db)):
    video = db.query(user_video.Video).get(video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video.clips


@router.get("/users/{user_id}/videos/{video_id}/clips/", response_model=list[schemas.VideoClip], summary="查询用户视频的所有切片")
def read_user_video_clips(user_id: int, video_id: int, db: Session = Depends(get_db)):
    user = db.query(user_video.User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    video = db.query(user_video.Video).filter(user_video.Video.id == video_id, user_video.Video.user_id == user_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    return video.clips


@router.get("/users/{user_id}/videos/clips/", response_model=list[schemas.VideoClip], summary="查询用户的所有视频切片")
def read_user_videos_clips(user_id: int, db: Session = Depends(get_db)):
    user = db.query(user_video.User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    clips = []
    for video in user.videos:
        clips.extend(video.clips)
    return clips
