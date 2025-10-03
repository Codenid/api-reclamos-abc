from sqlalchemy import Column, BigInteger, Integer, String, Date, TIMESTAMP, Text, ForeignKey
from src.api_reclamos.database import Base

class EvidenciaReclamo(Base):
    __tablename__ = "evidencias_reclamo"
    id_evidencia = Column(BigInteger, primary_key=True, autoincrement=True, index=True)  # BIGSERIAL
    id_reclamo = Column(BigInteger, ForeignKey("reclamos.id_reclamo", ondelete="CASCADE"), nullable=False)
    tipo_evidencia = Column(String(40), nullable=False)
    url_almacenamiento = Column(String(300))
    referencia_externa = Column(String(120))
    #metadatos = Column(Text)  # JSON en SQL; aquí texto simple
    fecha_agregado = Column(Date, nullable=False)
    agregado_por = Column(String(120))
    fecha_registro = Column(TIMESTAMP)