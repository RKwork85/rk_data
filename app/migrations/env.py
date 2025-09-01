from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import os
import sys

# 添加路径设置 - 这是关键修复
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.insert(0, root_dir)

# 现在可以安全导入应用模块
from app.models import Base
from app.database import engine

# 这是 Alembic 的配置对象，提供访问 .ini 文件中的值
config = context.config

# 设置目标元数据
target_metadata = Base.metadata

# 其他配置
def run_migrations_offline():
    """在 'offline' 模式下运行迁移"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_as_batch=True  # SQLite 需要这个选项
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """在 'online' 模式下运行迁移"""
    connectable = engine  # 使用我们定义的 engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=True  # SQLite 需要这个选项
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()