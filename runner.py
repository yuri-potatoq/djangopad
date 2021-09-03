import uvicorn

from core.asgi import application as app


if __name__ == "__main__":
    uvicorn.run("runner:app", host="0.0.0.0", port=8000, reload=True)