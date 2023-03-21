from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

@app.get('/')
async def index():
    return "hello from fastapi app"


if __name__ == '__main__':
    run(app, port=8080, host='0.0.0.0')