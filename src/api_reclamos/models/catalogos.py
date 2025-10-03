from sqlalchemy import Column, SmallInteger, Integer, String
from src.api_reclamos.database import Base

class TipoReclamo(Base):
    __tablename__ = "tipos_reclamo"
    id_tipo_reclamo = Column(SmallInteger, primary_key=True, autoincrement=True, index=True)
    codigo = Column(String(32), unique=True, nullable=False)
    nombre = Column(String(120), nullable=False)
    descripcion = Column(String(300))

class EstadoReclamo(Base):
    __tablename__ = "estados_reclamo"
    id_estado = Column(Integer, primary_key=True, autoincrement=True, index=True)  # BIGSERIAL en SQL
    codigo = Column(String(40), unique=True, nullable=False)
    nombre = Column(String(120), nullable=False)

class TipoRevisor(Base):
    __tablename__ = "tipos_revisor"
    id_tipo_revisor = Column(SmallInteger, primary_key=True, autoincrement=True, index=True)
    codigo = Column(String(32), unique=True, nullable=False)
    nombre = Column(String(120), nullable=False)
    descripcion = Column(String(300))