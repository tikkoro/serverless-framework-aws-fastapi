from fastapi import FastAPI
import sys
import os
from mangum import Mangum

app = FastAPI(
    root_path=f"/{os.environ['STAGE']}"
)
handler = Mangum(app)

@app.get("/hello")
async def hello():
    return {"message": "hello world!"}

@app.get("/ver")
async def ver():
    return {"python_ver": sys.version}
