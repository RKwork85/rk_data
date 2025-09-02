# app/migrations/env.py
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# 导入你的 Base 和所有模型
from app.models.base import Base
from app.models.user_video import *
from app.models.tasks import *

# Alembic 配置对象
config = context.config

# 设置日志
fileConfig(config.config_file_name)

# 设置目标 metadata，让 Alembic 知道要生成哪些表
target_metadata = Base.metadata

# 线上模式
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # ✅ 比较列类型变化
            compare_server_default=True,  # ✅ 比较默认值变化
        )

        with context.begin_transaction():
            context.run_migrations()


# 离线模式（生成 SQL 文件）
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        compare_server_default=True,
    )

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
