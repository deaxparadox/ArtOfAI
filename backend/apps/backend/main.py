from fastapi import APIRouter


# setup main application router `backend`
# representng the project name
backend_router = APIRouter()


@backend_router.get("/")
def backend_root():
    """
    Return the Welcome message
    """
    return {
        "message": "Welcome to ArtOfAI backend application"
    }