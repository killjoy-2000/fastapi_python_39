import uvicorn
from fastapi import FastAPI
from routes import login,validate_token,upload_file

app = FastAPI()

app.include_router(login.router)
app.include_router(validate_token.router)
app.include_router(upload_file.router)

# this will take effect if we use python run instead of uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
