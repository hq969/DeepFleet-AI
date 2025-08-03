from backend.models.delivery_model import Delivery, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///fleet.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

session.add(Delivery(location="A", lat=12.9, lon=77.5))
session.commit()
