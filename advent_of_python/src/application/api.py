import uvicorn
from fastapi import FastAPI

from application import endpoints
from application.container import Container
from application.endpoints import router


def make_application() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app




if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__, endpoints])
    app = make_application()
    uvicorn.run(app, port=8080)
