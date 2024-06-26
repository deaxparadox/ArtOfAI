from typing import Union

from fastapi import FastAPI

from backend.apps.backend.main import backend_router
from backend.apps.data.main import data_router

app = FastAPI()

app.include_router(backend_router)
app.include_router(data_router)