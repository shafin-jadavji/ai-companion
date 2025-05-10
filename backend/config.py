from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    use_memory: bool = True
    debug: bool = False
    default_personality: str = "supportive"

    class Config:
        env_file = ".env"

settings = Settings()
