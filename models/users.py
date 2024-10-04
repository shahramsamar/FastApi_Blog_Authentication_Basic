from sqlalchemy import Column, String, DateTime, Enum, Integer
import datetime, bcrypt
from core.config_database.database import Base




class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(Enum("user", "admin",name="user_roles"), nullable=False )
    email = Column(String(255), nullable=False)
    _password = Column(String(255), nullable=False)
    created_date = Column(DateTime, nullable=False,default=datetime.datetime.now())
    updated_date = Column(DateTime, nullable=False, default=datetime.datetime.now(), onupdate=datetime.datetime.now()) 

    def __str__(self):
       return self.user

 
    # Password property
    @property
    def password(self):
        return self._password
    
    # Setter to hash password before saving
    @password.setter
    def password(self, raw_password):
        hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())  # Hash the password
        self._password = hashed_password.decode('utf-8')  # Store the hashed password

    # Method to verify password
    def verify_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf-8'), self._password.encode('utf-8'))