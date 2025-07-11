from fastapi import FastAPI
from routes import auth_routes,order_routes

app = FastAPI()

app.include_router(auth_routes.auth_router)
app.include_router(order_routes.order_router)

