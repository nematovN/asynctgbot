import aiosqlite
from datetime import datetime


DB_NAME = "users.db"


async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                joined_at TEXT
            )
        """)
        await db.commit()


async def add_user(user_id: int, username: str, first_name: str, last_name: str | None):
    async with aiosqlite.connect(DB_NAME) as db:
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        await db.execute("""
            INSERT OR REPLACE INTO users (user_id, username, first_name, last_name, joined_at)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, username, first_name, last_name, now))
        await db.commit()


async def get_user_count() -> int:
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT COUNT(*) FROM users") as cursor:
            (count,) = await cursor.fetchone()
            return count
