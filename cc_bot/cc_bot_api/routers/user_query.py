from fastapi import FastAPI, APIRouter


router = APIRouter(prefix="/ccbot", tags=["Credit Card Bot"])



@router.get("/user_query")
def get_user_response():
    return "I am good"