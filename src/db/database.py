from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Update with your actual MySQL credentials
DATABASE_URL = "mysql+mysqlconnector://root:deepak@localhost:3306/land_broker_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
