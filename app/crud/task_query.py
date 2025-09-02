from sqlalchemy.orm import Session
from app.models.frontend_rbg import FrontendRBGTask, TaskListener

class TaskQuery:
    def __init__(self, db: Session):
        self.db = db

    def get_tasks_by_user(self, user_name: str):
        """
        根据用户名查询该用户所有任务及状态
        返回列表，每个元素为字典：
        {
            "taskID": str,
            "taskType": str,
            "data": dict,
            "taskStatus": str,
            "taskResult": dict
        }
        """
        tasks = (
            self.db.query(FrontendRBGTask)
            .join(TaskListener)
            .filter(FrontendRBGTask.userName == user_name)
            .all()
        )

        result = []
        for task in tasks:
            listener = task.listener
            result.append({
                "taskID": task.taskID,
                "taskType": task.taskType,
                "data": task.data,
                "taskStatus": listener.taskStatus if listener else None,
                "taskResult": listener.taskResult if listener else None,
            })
        return result

    def get_user_by_status(self, task_status: str):
        """
        根据任务状态查询所有对应用户
        返回列表，每个元素为字典：
        {
            "userName": str,
            "taskID": str,
            "taskType": str,
            "data": dict,
            "taskResult": dict
        }
        """
        listeners = (
            self.db.query(TaskListener)
            .join(FrontendRBGTask)
            .filter(TaskListener.taskStatus == task_status)
            .all()
        )

        result = []
        for listener in listeners:
            task = listener.task
            result.append({
                "userName": task.userName if task else None,
                "taskID": task.taskID if task else None,
                "taskType": task.taskType if task else None,
                "data": task.data if task else None,
                "taskResult": listener.taskResult,
            })
        return result



'''
用法示例：
from app.database import get_db

with get_db() as db:
    tq = TaskQuery(db)
    
    # 1️⃣ 查询用户所有任务
    tasks = tq.get_tasks_by_user("alice")
    print(tasks)

    # 2️⃣ 根据任务状态查询用户
    users = tq.get_user_by_status("completed")
    print(users)



新建文件 app/crud/task_query.py

把 TaskQuery 类粘贴进去

在需要查询的地方导入

例如在你的 tasks.py API 文件里：

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.task_query import TaskQuery
from app.database import get_db

router = APIRouter()

@router.get("/user_tasks/{user_name}")
def get_user_tasks(user_name: str, db: Session = Depends(get_db)):
    tq = TaskQuery(db)
    return tq.get_tasks_by_user(user_name)

'''