import sys
import os
import asyncio
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import engine, Base
from model.models import User, Order  # Add your models if needed
from sqlmodel import create_engine, text, SQLModel

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())

