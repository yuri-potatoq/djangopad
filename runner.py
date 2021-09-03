import uvicorn

from core.asgi import application as app


if __name__ == "__main__":
    run_conf = {
        'app': "runner:app", 
        'host': "0.0.0.0", 
        'port': 8000, 
        'reload': True,
        'forwarded_allow_ips': '*',
        'timeout_keep_alive': 0,
        'limit_max_requests': 0,
    }

    uvicorn.run(**run_conf)