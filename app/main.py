from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db, engine

# 创建数据库表（开发环境使用，生产环境使用迁移）
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="🎬 视频处理模块数据接口服务",
    description=(
        "📤 提供视频上传、切片、查询等能力的 RESTful 服务。\n\n"
        "👤 对视频处理服务的用户信息及视频信息提供数据支持\n\n"
        "📦 支持大文件分片上传\n\n"
        "✂️ 自动生成可播放切片\n\n"
        "🔔 实时回调通知\n\n"
        "⚡ Powered by FastAPI + SQLAlchemy + Alembic"
    ),
    version="rkwork:1.0.0",
)


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 检查用户名是否唯一
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/users/{user_id}/videos/", response_model=schemas.Video)
def create_video(
    user_id: int, 
    video: schemas.VideoCreate, 
    db: Session = Depends(get_db)
):
    # 验证用户存在
    user = db.query(models.User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_video = models.Video(**video.dict(), user_id=user_id)
    db.add(new_video)
    db.commit()
    db.refresh(new_video)
    return new_video

@app.post("/videos/{video_id}/clips/", response_model=schemas.VideoClip)
def create_clip(
    video_id: int, 
    clip: schemas.VideoClipCreate, 
    db: Session = Depends(get_db)
):
    # 验证视频存在
    video = db.query(models.Video).get(video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    new_clip = models.VideoClip(**clip.dict(), video_id=video_id)
    db.add(new_clip)
    db.commit()
    db.refresh(new_clip)
    return new_clip


@app.get("/users/count/", response_model=int)
def get_user_count(db: Session = Depends(get_db)):
    user_count = db.query(models.User).count()  # 查询用户表的总记录数
    return user_count  # 返回用户总数


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/videos/{video_id}", response_model=schemas.Video)
def read_video(video_id: int, db: Session = Depends(get_db)):
    video = db.query(models.Video).get(video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video

@app.get("/videos/{video_id}/clips/", response_model=list[schemas.VideoClip])
def read_clips(video_id: int, db: Session = Depends(get_db)):
    video = db.query(models.Video).get(video_id)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    return video.clips


# 查询某个用户的所有视频
@app.get("/users/{user_id}/videos/", response_model=list[schemas.Video])
def read_user_videos(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user.videos  # 返回该用户的所有视频

# 查询某个用户的某个视频的所有切片
@app.get("/users/{user_id}/videos/{video_id}/clips/", response_model=list[schemas.VideoClip])
def read_user_video_clips(user_id: int, video_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    video = db.query(models.Video).filter(models.Video.id == video_id, models.Video.user_id == user_id).first()
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    return video.clips  # 返回该视频的所有切片

# 查询某个用户的所有视频的所有切片
@app.get("/users/{user_id}/videos/clips/", response_model=list[schemas.VideoClip])
def read_user_videos_clips(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    clips = []
    for video in user.videos:
        clips.extend(video.clips)  # 将所有视频的切片添加到返回结果中
    
    return clips  # 返回该用户所有视频的所有切片