from sqlalchemy.orm import Session
from src.api_reclamos.database import SessionLocal

def get_db():
    """Dependencia para obtener y cerrar la sesión de BD por request."""
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()