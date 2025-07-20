from fastapi import FastAPI
from src.routers import  plots # , users
# from src.routers import users  # Uncomment if users router is available

# from routers import users, plots
from src.db.database import Base, engine
import src.models.plot

app = FastAPI()
# app.include_router(users.router)
app.include_router(plots.router)



Base.metadata.create_all(bind=engine)

