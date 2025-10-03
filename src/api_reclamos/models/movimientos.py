from sqlalchemy import Column, BigInteger, Integer, String, Date, TIMESTAMP, ForeignKey, UniqueConstraint
from src.api_reclamos.database import Base

class MovimientoReclamo(Base):
    __tablename__ = "movimientos_reclamo"
    id_movimiento = Column(BigInteger, primary_key=True, autoincrement=True, index=True)  # BIGSERIAL
    id_reclamo = Column(BigInteger, ForeignKey("reclamos.id_reclamo", ondelete="CASCADE"), nullable=False)
    id_movimiento_externo = Column(String(80), nullable=False)
    sistema_origen = Column(String(60), nullable=False)
    fecha_vinculo = Column(Date, nullable=False)
    fecha_registro = Column(TIMESTAMP)

    __table_args__ = (
        UniqueConstraint("id_reclamo", "id_movimiento_externo", "sistema_origen", name="uq_mov_ext_origen"),
    )