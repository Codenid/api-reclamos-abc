from sqlalchemy import Column, BigInteger, Integer, SmallInteger, String, Date, Numeric, Text, TIMESTAMP, ForeignKey #, MetaData
from src.api_reclamos.database import Base
#from sqlalchemy.ext.declarative import declarative_base

#Base = declarative_base(metadata=MetaData(schema="gestion_reclamos"))

class Reclamo(Base):
    __tablename__ = "reclamos"
    id_reclamo = Column(BigInteger, primary_key=True, autoincrement=True, index=True)  # BIGSERIAL
    id_cliente = Column(Integer, nullable=False)
    id_producto = Column(Integer, nullable=False)
    id_tipo_reclamo = Column(SmallInteger, ForeignKey("tipos_reclamo.id_tipo_reclamo"), nullable=False)
    id_estado_actual = Column(Integer, ForeignKey("estados_reclamo.id_estado"), nullable=False)  # BIGINT en SQL
    fecha_apertura = Column(Date, nullable=False)
    fecha_cierre = Column(Date)
    canal = Column(String(32))
    referencia_externa = Column(String(64), unique=True, nullable=False)
    descripcion = Column(Text)
    monto = Column(Numeric(10, 2))
    moneda = Column(String(3))
    fecha_actualizacion = Column(TIMESTAMP)