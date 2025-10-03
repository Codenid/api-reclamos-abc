from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.api_reclamos.config import settings

# Motor de base de datos
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    future=True
)

# Sesiones
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

# MetaData con esquema global
metadata = MetaData(schema="gestion_reclamos")

class Base(DeclarativeBase):
    """Base declarativa de SQLAlchemy."""
    metadata = metadata
    pass