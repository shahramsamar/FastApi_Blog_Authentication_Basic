from pydantic_settings  import BaseSettings

# postgresql://user:password@host:port/db_name

class Settings(BaseSettings):
    DATABASE_URL : str = "sqlite:///./sqlite.db"

settings = Settings()    