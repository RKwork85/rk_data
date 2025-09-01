# main.py
from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    # 大标题（浏览器标签 & ReDoc 左上角）
    title="Video Service API",
    # 一句话简介（OpenAPI info.description）
    description=(
        "提供视频上传、切片、查询等能力的 RESTful 服务。\n\n"
        "- 支持大文件分片上传  \n"
        "- 自动生成可播放切片  \n"
        "- 实时回调通知  \n\n"
        "⚡ Powered by FastAPI + SQLAlchemy + Alembic"
    ),
    # 版本号
    version="1.0.0",
    # 默认根路径（如使用反向代理，可改成 /api/v1）
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    # 统一的标签分组
    tags=[
        {"name": "system",  "description": "系统通用接口"},
        {"name": "videos",  "description": "视频管理"},
        {"name": "clips",   "description": "切片管理"},
    ],
)

# ---------- 示例路由 ----------
@app.get(
    "/",
    tags=["system"],
    summary="系统初始页",
    description="返回一条欢迎信息，可用于健康检查。"
)
def root():
    return {"message": "Welcome to Video Service API", "timestamp": datetime.utcnow()}