from fastapi import FastAPI
from routers import users, plots
from db.database import Base, engine
import models.plot

app = FastAPI()
app.include_router(users.router)
app.include_router(plots.router)



Base.metadata.create_all(bind=engine)

