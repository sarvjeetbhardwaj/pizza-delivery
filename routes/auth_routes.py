from fastapi import APIRouter


auth_router = APIRouter(prefix='/auth',tags=['auth'])

@auth_router.get('/')
async def check_health():
    return {'auth_router': 'healthy'}