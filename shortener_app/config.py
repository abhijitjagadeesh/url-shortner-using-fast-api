from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Base settings for the project."""

    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortner.db"

    class Config:
        """Override the default configs values from values in .env file."""

        env_file = ".env"


@lru_cache  # to optimize the get_setting func using the lru cache
def get_settings() -> Settings:
    """Get the project settings values."""
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
