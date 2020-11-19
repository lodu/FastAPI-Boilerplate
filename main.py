from fastapi import FastAPI
from src.routes import router
from src.config import SYSTEM_NAME

from fastapi.middleware.cors import CORSMiddleware

# I would strongly suggest you to change this
app = FastAPI(title=f"API For {SYSTEM_NAME}", description="Visit <URL>/docs for docs")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# You can change this prefix, but beware of the nginx.conf
app.include_router(router, prefix="/api")
