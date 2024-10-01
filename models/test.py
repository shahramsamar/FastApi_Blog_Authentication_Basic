from sqlalchemy import Column, String, DateTime, Enum, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError
import datetime
import bcrypt

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(Enum("user", "admin", name="user_roles"), nullable=False)
    email = Column(String(255), nullable=False, unique=True)  # Unique email
    _password = Column(String(255), nullable=False)
    created_date = Column(DateTime, nullable=False, default=datetime.datetime.now)  # Current time when created
    updated_date = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)  # Current time on update

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

# Database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"

# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

# Function to create a new user
def create_user(user_role, email, password):
    with SessionLocal() as db:
        try:
            user_obj = Users(
                user=user_role,
                email=email,
            )
            user_obj.password = password  # This will hash the password
            db.add(user_obj)
            db.commit()
        except IntegrityError as e:
            db.rollback()  # Roll back in case of error
            print("Integrity error, likely due to unique constraint:", e)
        except Exception as e:
            db.rollback()  # Roll back in case of error
            print(f"Error occurred: {e}")

# Example usage
create_user("user", "test@example.com", "my_secure_password")
create_user("admin", "admin@example.com", "admin_password")

# # Verify password example
# with SessionLocal() as session:
#     user = session.query(Users).filter_by(email="admin@example.com").first()
#     if user and user.verify_password("admin_password"):
#         print("Password verified!")
#     else:
#         print("Password verification failed.")
