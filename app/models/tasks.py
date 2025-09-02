"""
* @Description: 前端_rbg任务记录表 - SQLAlchemy ORM模型
* @Author: rkwork
* @Date: 2025-09-02
"""
"""
* @Description: 前端_rbg任务记录表 - SQLAlchemy ORM模型
* @Author: rkwork
* @Date: 2025-09-02
"""
from datetime import datetime, date
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from app.models.base import Base

def today_date():
    """
    返回当天的日期（去掉时分秒），只保留年月日
    """
    return datetime.now().replace(microsecond=0)

class FrontendRBGTask(Base):
    __tablename__ = "frontend_rbg_task_submit"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userName = Column(String(50), nullable=False, index=True, comment="用户名")
    taskID = Column(String(100), nullable=False, unique=True, comment="任务ID")
    taskType = Column(String(50), nullable=False, comment="任务类型")
    data = Column(Text, nullable=True, comment="任务附加数据")
    dateTime = Column(DateTime, default=today_date(), comment="创建时间")

    # 一对一关系：一个任务对应一个 listener
    listener = relationship("TaskListener", back_populates="task", uselist=False, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<FrontendRBGTask(userName={self.userName}, taskID={self.taskID}, taskType={self.taskType}, dateTime={self.dateTime})>"

class TaskListener(Base):
    __tablename__ = "task_listener"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    taskID = Column(String(100), ForeignKey("frontend_rbg_task_submit.taskID"), nullable=False, unique=True, comment="任务ID")
    taskStatus = Column(String(50), nullable=False, index=True, comment="任务状态")
    taskResult = Column(Text, nullable=True, comment="任务结果")

    # 反向关系
    task = relationship("FrontendRBGTask", back_populates="listener")
