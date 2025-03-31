from fastapi import FastAPI, Request
from router import router
import uvicorn
from schemas import config_emulate

from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(router)

Instrumentator().instrument(app).expose(app, endpoint='/metrics/actuator')

if __name__ == "__main__":
    uvicorn.run(app, host=config_emulate.HOST, port=config_emulate.PORT, limit_concurrency=config_emulate.MAX_USERS)