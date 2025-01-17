import uvicorn
from fastapi import FastAPI
from database import Sessionlocal, engine, Base
from routers import user as UserRouter

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(UserRouter.router, prefix="/user")


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, workers=3)