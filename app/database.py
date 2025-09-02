from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"  # 例子，换成你的数据库URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # 仅 sqlite 需要
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 依赖注入函数
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
