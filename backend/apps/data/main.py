from typing import Optional
from fastapi import APIRouter

data_router = APIRouter(
    prefix="/data",
    tags=['data']
)

@data_router.get("/")
def data_root(q: Optional[str] = None):
    if q != None:
        return {
            "message": "returning the {} data".format(q)
        }
    else:
        return {
            "message": "Welcome to data application."
        }