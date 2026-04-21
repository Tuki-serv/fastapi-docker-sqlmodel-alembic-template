from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import model_validator
import os

class Settings(BaseSettings):
    # Campo unico (con default:opcional)
    DATABASE_URL: str = "postgresql+psycopg://postgres:lucas@localhost:5432/appdb"

    @model_validator(mode="after")
    def fix_database_url(self):
        if self.DATABASE_URL and self.DATABASE_URL.startswith("postgresql://"):
            self.DATABASE_URL = self.DATABASE_URL.replace("postgreslq://","postgresql+psycopg://",1)
            return self
    
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
