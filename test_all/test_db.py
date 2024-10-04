from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
import datetime

# Database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"

# Create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define base class
Base = declarative_base()



# Define Task model
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    is_done = Column(Boolean, default=False)
    created_date = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))

    def __str__(self):
        return f"{self.id} - {self.title}"

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Create a new session
db = SessionLocal()

# Create a new task object
task_obj = Task(title="No 2")

# Add and commit the new task
db.add(task_obj)
db.commit()

# Optional: refresh the object to reflect the committed state
# db.refresh(task_obj)

# Close the session
# db.close()

# Output the task object
# print(task_obj)


# task_obj = Task(title="al")

# db = SessionLocal()
# # adding object example
# db.add(task_obj)
# db.commit()
# db.refresh(task_obj)

# query all objects example
# tasks = db.query(Task).all()
# for task in tasks:
#     print(task)

# tasks =db.query(Task).filter(Task.is_done ==False)
# for task in tasks:
#     print(task)

# get one object
# task_obj  = db.query(Task).filter(Task.id==5,Task.is_done == False).one_or_none()
# print(task_obj)

# update
# task_obj.is_done = True
# db.commit()
# db.refresh(task_obj)


# deleting object
# task_obj  = db.query(Task).filter(Task.id==5).one_or_none()
# print(task_obj)

# db.delete(task_obj)
# db.commit()

# for check database to initiate 
# def initiate_database():
#     Base.metadata.create_all(bind=engine)

