from pathlib import Path
import os
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent

UPLOAD_DIR = BASE_DIR / "test_photo"
os.makedirs(UPLOAD_DIR, exist_ok=True)


class Settings(BaseSettings):
    EMAIL_ADDRESS: str
    EMAIL_PASSWORD: str

    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/save_bd_backup1.db"

    # class Settings(BaseSettings):
    # DB_HOST: str
    # DB_PORT: int
    # DB_USER: str
    # DB_PASS: str
    # DB_NAME: str

    # @property
    # def DATABASE_URL_asyncpg(self):
    #     # postgresql+asyncpg://postgres:postgres@localhost:5432/sa
    #     return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env")


settings = Settings()
