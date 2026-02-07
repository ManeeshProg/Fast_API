from fastapi import FastAPI
from routers import users, car
app = FastAPI()

app.include_router(car.router, prefix="/cars", tags=["cars"])
app.include_router(users.router, prefix="/users", tags=["users"])
@app.get("/")
async def root():
    return {"message": "Hello World"}