from fastapi import FastAPI
from app.database import engine
from app.models.base import Base
from app.apis.v1.endpoints import videos, tasks  # 导入路由模块


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

# 路由注册
app.include_router(videos.router, prefix="/api/v1/videos", tags=["Videos"])
app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {"message": "Welcome to Video Processing API!"}
