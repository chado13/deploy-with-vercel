from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI on Vercel!"}

# Vercel의 서버리스 환경에서 FastAPI를 실행하기 위한 핸들러
handler = Mangum(app)