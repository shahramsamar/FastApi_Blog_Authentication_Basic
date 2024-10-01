from sqlalchemy import Column, String, DateTime, Enum, Integer
import datetime
from sqlalchemy.orm import  declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(Enum("user", "admin",name="user_roles"), nullable=False )
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created_date = Column(DateTime, nullable=False,default=datetime.datetime.now())
    updated_date = Column(DateTime, nullable=False, default=datetime.datetime.now(), onupdate=datetime.datetime.now()) 

    def __str__(self):
       return self.user

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker


# # Database URL
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"


# # Create engine
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )


# # Create session
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# # Create a new session
# db = SessionLocal()

# # Create a new user with role 'user'
# user_obj = Users(
#     user="admin",                 # This should be 'user' or 'admin' as per your Enum
#     email="shahramsamar2010@gmail.com",     # Provide a valid email
#     password="Aa123456",   # Provide a hashed password (hash this before saving)
# )

# # Add and commit the new user
# db.add(user_obj)
# db.commit()

# # Close the session after committing
# db.close()

    