from fastapi import FastAPI
from routers import user, task

# python -m uvicorn main:app

app = FastAPI()


@app.get('/')
async def welcome():
    return {'message': 'Welcome to Taskmanager'}

app.include_router(user.router)
app.include_router(task.router)

