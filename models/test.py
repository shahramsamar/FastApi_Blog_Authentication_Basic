# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, String, DateTime, Enum, Integer
# import datetime

# # Define the Base for your models
# Base = declarative_base()

# # Define the Users model
# class Users(Base):
#     __tablename__ = "users"
    
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user = Column(Enum("user", "admin", name="user_roles"), nullable=False)
#     email = Column(String(255), nullable=False, unique=True)  # Ensure email is unique
#     password = Column(String(255), nullable=False)  # Store hashed passwords
#     created_date = Column(DateTime, nullable=False, default=lambda: datetime.datetime.now().replace(second=0, microsecond=0))
#     updated_date = Column(DateTime, nullable=False, default=lambda: datetime.datetime.now().replace(second=0, microsecond=0), onupdate=lambda: datetime.datetime.now().replace(second=0, microsecond=0))

# # Database URL
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"

# # Create engine
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# # Create session
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Create tables
# Base.metadata.create_all(bind=engine)

# # Function to create a new user
# def create_user(user_role, email, password):
#     # Create a new session
#     db = SessionLocal()

#     # Create a new user object
#     user_obj = Users(
#         user=user_role,                 # This should be 'user' or 'admin' as per your Enum
#         email=email,                    # Provide a valid email
#         password=password                # Store a hashed password (hash this before saving)
#     )

#     # Add and commit the new user
#     db.add(user_obj)
#     db.commit()

#     # Close the session after committing
#     db.close()

# # Example usage
# create_user("user", "shahramsamar2010@gmail.com", "Aa123456")
from sqlalchemy import Column, String, DateTime, Enum, Integer
import datetime
from sqlalchemy.orm import  declarative_base,sessionmaker
from sqlalchemy import create_engine

# Database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"


# Create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


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




def create_user(user_role, email, password):
    db = SessionLocal()
    user_obj = Users(
        user=user_role,                 # This should be 'user' or 'admin' as per your Enum
        email=email,                    # Provide a valid email
        password=password                # Store a hashed password (hash this before saving)
    )
    db.add(user_obj)
    db.commit()
    db.close()

create_user("user", "test", "test")
    