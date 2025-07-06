import sys
import os
import asyncio
from database import engine, Base
from models import User, Order  # Add your models if needed
from sqlmodel import create_engine, text, SQLModel

async def init_db():
    #print(Base.metadata.tables.keys())
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())

