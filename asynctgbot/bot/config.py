from pydantic import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    admin_id: int = 0

    class Config:
        env_file = ".env"


settings = Settings()
