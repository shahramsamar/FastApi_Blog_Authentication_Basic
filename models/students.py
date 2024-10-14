from sqlalchemy import  Column, Integer, String, Boolean, DateTime
import datetime
from database.database import Base


# Define Task model
class StudentModel(Base):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    # is_done = Column(Boolean, default=False)
    # created_date = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))

    def __str__(self):
        return f"{self.id} - {self.name}"



