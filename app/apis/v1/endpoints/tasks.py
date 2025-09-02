"""
* @Description: 任务提交 & 监听接口
* @Author: rkwork
* @Date: 2025-09-02
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.tasks import FrontendRBGTask, TaskListener
from app.database import get_db
from pydantic import BaseModel
from typing import Any, Dict, Optional
import json  # <-- 新增

router = APIRouter()

# =====================
# Pydantic Schemas
# =====================
class TaskSubmitSchema(BaseModel):
    userName: str
    taskID: str
    taskType: str
    data: Optional[Dict[str, Any]] = None  # 可选字典

class TaskListenerSchema(BaseModel):
    taskID: str
    taskStatus: str
    taskResult: Optional[Dict[str, Any]] = None  # 可选字典

# =====================
# 接口定义
# =====================
@router.post("/frontend_rbg_task_submit", summary="提交前端任务")
def submit_frontend_task(task: TaskSubmitSchema, db: Session = Depends(get_db)):
    """前端任务提交接口"""
    existing_task = db.query(FrontendRBGTask).filter(FrontendRBGTask.taskID == task.taskID).first()
    if existing_task:
        raise HTTPException(status_code=400, detail="任务ID已存在")

    new_task = FrontendRBGTask(
        userName=task.userName,
        taskID=task.taskID,
        taskType=task.taskType,
        data=json.dumps(task.data) if task.data else None  # <-- 最小改动
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {"message": "任务提交成功", "taskID": new_task.taskID}
@router.get("/frontend_rbg_tasks_by_user/{userName}", summary="根据用户名查询所有任务")
def get_tasks_by_user(userName: str, db: Session = Depends(get_db)):
    """
    根据用户名查询该用户提交的所有前端任务
    """
    tasks = db.query(FrontendRBGTask).filter(FrontendRBGTask.userName == userName).all()
    if not tasks:
        raise HTTPException(status_code=404, detail="未找到该用户的任务")

    result = []
    for t in tasks:
        result.append({
            "taskID": t.taskID,
            "taskType": t.taskType,
            "data": json.loads(t.data) if t.data else None,  # 反序列化 JSON
            "dateTime": t.dateTime.strftime("%Y-%m-%d %H:%M:%S")  # 格式化时间
        })

    return {"userName": userName, "tasks": result}


@router.get("/frontend_rbg_tasks_full/{userName}", summary="根据用户名查询所有任务及状态信息")
def get_tasks_full_by_user(userName: str, db: Session = Depends(get_db)):
    """
    查询指定用户的所有任务及对应监听状态
    """
    tasks = db.query(FrontendRBGTask).filter(FrontendRBGTask.userName == userName).all()
    if not tasks:
        raise HTTPException(status_code=404, detail="未找到该用户的任务")

    result = []
    for t in tasks:
        listener = t.listener  # relationship 一对一
        result.append({
            "taskID": t.taskID,
            "taskType": t.taskType,
            "data": json.loads(t.data) if t.data else None,        # 反序列化 JSON
            "dateTime": t.dateTime.strftime("%Y-%m-%d %H:%M:%S"), # 格式化时间
            "taskStatus": listener.taskStatus if listener else None,
            "taskResult": json.loads(listener.taskResult) if listener and listener.taskResult else None
        })

    return {"userName": userName, "tasks": result}


@router.post("/task_listener", summary="提交任务监听信息")
def submit_task_listener(listener: TaskListenerSchema, db: Session = Depends(get_db)):
    """任务监听提交接口"""
    task = db.query(FrontendRBGTask).filter(FrontendRBGTask.taskID == listener.taskID).first()
    if not task:
        raise HTTPException(status_code=404, detail="未找到对应的任务ID")

    existing_listener = db.query(TaskListener).filter(TaskListener.taskID == listener.taskID).first()
    if existing_listener:
        existing_listener.taskStatus = listener.taskStatus
        existing_listener.taskResult = json.dumps(listener.taskResult) if listener.taskResult else None  # <-- 改动
        db.commit()
        db.refresh(existing_listener)
        return {"message": "任务监听更新成功", "taskID": listener.taskID}

    new_listener = TaskListener(
        taskID=listener.taskID,
        taskStatus=listener.taskStatus,
        taskResult=json.dumps(listener.taskResult) if listener.taskResult else None  # <-- 改动
    )
    db.add(new_listener)
    db.commit()
    db.refresh(new_listener)

    return {"message": "任务监听提交成功", "taskID": new_listener.taskID}
