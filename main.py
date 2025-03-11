import uvicorn
from fastapi.responses import HTMLResponse #used to return HTML response
from fastapi import Depends, FastAPI #Depends is used to manage dependencies like authentication while fastapi is the main class
from routers import user

app = FastAPI()

app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
