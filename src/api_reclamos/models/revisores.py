from sqlalchemy import Column, SmallInteger, BigInteger, Integer, String, Date, TIMESTAMP, ForeignKey
from src.api_reclamos.database import Base

class Revisor(Base):
    __tablename__ = "revisores"
    id_revisor = Column(SmallInteger, primary_key=True, autoincrement=True, index=True)
    id_tipo_revisor = Column(SmallInteger, ForeignKey("tipos_revisor.id_tipo_revisor"), nullable=False)
    nombre_completo = Column(String(160), nullable=False)
    correo = Column(String(160), nullable=False)
    activo = Column(Integer, nullable=False)  # BOOLEAN en SQL; mapeado simple

class RevisorReclamo(Base):
    __tablename__ = "revisores_reclamo"
    id_asignacion = Column(BigInteger, primary_key=True, autoincrement=True, index=True)  # BIGSERIAL
    id_reclamo = Column(BigInteger, ForeignKey("reclamos.id_reclamo", ondelete="CASCADE"), nullable=False)
    id_revisor = Column(SmallInteger, ForeignKey("revisores.id_revisor"), nullable=False)
    fecha_asignacion = Column(Date, nullable=False)
    decision = Column(String(40))
    fecha_decision = Column(Date)
    nota = Column(String(500))
    fecha_registro = Column(TIMESTAMP)