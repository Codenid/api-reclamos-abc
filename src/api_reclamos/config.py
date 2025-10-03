import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Configuración de variables de entorno."""
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

settings = Settings()