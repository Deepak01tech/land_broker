from src.models import Plot
# D:\my_projects\land_broker\src\models\plot.py
from sqlalchemy.orm import Session

def create_plot(db: Session, plot_data):
    new_plot = Plot(**plot_data.dict())
    db.add(new_plot)
    db.commit()
    db.refresh(new_plot)
    return new_plot

def get_all_plots(db: Session):
    return db.query(Plot).all()
