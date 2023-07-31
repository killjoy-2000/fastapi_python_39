import uvicorn
from fastapi import FastAPI
from routes import login

app = FastAPI()

app.include_router(login.router)

# this will take effect if we use python run instead of uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
