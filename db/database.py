from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
import os

load_dotenv()

engine = AsyncEngine(
   create_engine(
        url = os.getenv('DATABASE_URL'),
        echo=True,
    )
)

Base = declarative_base()

Session = sessionmaker()