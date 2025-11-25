from fastapi import FastAPI

# from src.routers import users  # Uncomment if users router is available

# from routers import users, plots
from src.db.database import Base, engine

from src.models import User, Plot
from src.routers import  plots # , users
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import user  # import your router
import src.models.plot

app = FastAPI()
Base.metadata.create_all(bind=engine)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(users.router)
app.include_router(plots.router)





