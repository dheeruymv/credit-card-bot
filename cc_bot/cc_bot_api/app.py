from fastapi import FastAPI, APIRouter
from uvicorn import run
from routers import user_query


def main():
    app = FastAPI()
    app.include_router(user_query.router)
    run(app)




if __name__ == '__main__':
    main()