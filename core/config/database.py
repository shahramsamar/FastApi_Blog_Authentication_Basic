from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
import datetime
from .config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Define Task model
class StudentModel(Base):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    # is_done = Column(Boolean, default=False)
    # created_date = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))

    def __str__(self):
        return f"{self.id} - {self.name}"



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# for check database to initiate         
def initiate_database():
    Base.metadata.create_all(bind=engine)