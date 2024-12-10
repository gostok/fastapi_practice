from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://test_postgres:postgres@localhost:5432/fastapi_practice_db",
)  # postgresql+asyncpg - чтобы алхимия подключалась асинхронно
