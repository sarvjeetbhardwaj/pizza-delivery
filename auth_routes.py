from fastapi import APIRouter, status, HTTPException
from database import Session, engine
from schemas import SignUpModel
from models import User
from sqlalchemy.future import select
from werkzeug.security import generate_password_hash

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.get('/')
async def hello():
    return {'message': 'Hello World'}

@auth_router.post('/signup', response_model=SignUpModel, status_code=status.HTTP_201_CREATED)
async def signup(user: SignUpModel):
    async with Session() as session:
        # Check email
        result = await session.execute(select(User).where(User.email == user.email))
        db_email = result.scalars().first()
        if db_email is not None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='User with the email already exists')

        # Check username
        result = await session.execute(select(User).where(User.username == user.username))
        db_username = result.scalars().first()
        if db_username is not None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='User with the username already exists')

        new_user = User(
            username=user.username,
            email=user.email,
            password=generate_password_hash(user.password),
            is_active=user.is_active,
            is_staff=user.is_staff
        )
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user