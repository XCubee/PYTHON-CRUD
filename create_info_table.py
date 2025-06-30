from database import db
from models import Info, Base

db.connect()
Base.metadata.create_all(bind=db.engine)
print("Tables created!") 