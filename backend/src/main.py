from fastapi import FastAPI

# from src.routers import users  # Uncomment if users router is available

# from routers import users, plots
from src.db.database import Base, engine

from src.models import User, Plot
from src.routers import  plots # , users

import src.models.plot

app = FastAPI()
Base.metadata.create_all(bind=engine)

# app.include_router(users.router)
app.include_router(plots.router)





