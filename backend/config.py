from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    use_memory: bool = True
    default_personality: str = "supportive"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()

# Logging configuration
import logging
from logging.handlers import RotatingFileHandler
import sys

LOG_FILE = "logs/ai_companion.log"

log_formatter = logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=5)
file_handler.setFormatter(log_formatter)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(log_formatter)

# Explicit root logger configuration (reliable)
root_logger = logging.getLogger()
root_logger.setLevel(getattr(logging, settings.log_level.upper(), logging.INFO))
root_logger.addHandler(file_handler)
root_logger.addHandler(stream_handler)
