from fastapi import APIRouter

order_router = APIRouter(prefix='/order',tags=['orders'])

@order_router.get('/')
async def health_check():
    return {'message' : 'healthy'}