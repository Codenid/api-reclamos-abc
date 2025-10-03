from sqlalchemy import Column, BigInteger, SmallInteger, Integer, Date, TIMESTAMP, ForeignKey, String
from src.api_reclamos.database import Base

class HistorialEstado(Base):
    __tablename__ = "historial_estados"
    id_historial = Column(BigInteger, primary_key=True, autoincrement=True, index=True)  # BIGSERIAL
    id_reclamo = Column(BigInteger, ForeignKey("reclamos.id_reclamo", ondelete="CASCADE"), nullable=False)
    id_estado_origen = Column(Integer, ForeignKey("estados_reclamo.id_estado"))
    id_estado_destino = Column(Integer, ForeignKey("estados_reclamo.id_estado"), nullable=False)
    fecha_cambio = Column(Date, nullable=False)
    usuario_cambio = Column(String(120))
    nota = Column(String(500))
    fecha_registro = Column(TIMESTAMP)

class EquipoBackoffice(Base):
    __tablename__ = "equipos_backoffice"
    id_equipo = Column(SmallInteger, primary_key=True, autoincrement=True, index=True)
    codigo = Column(String(32), unique=True, nullable=False)
    nombre = Column(String(160), nullable=False)
    descripcion = Column(String(300))

class Analista(Base):
    __tablename__ = "analistas"
    id_analista = Column(SmallInteger, primary_key=True, autoincrement=True, index=True)
    codigo_empleado = Column(String(32), unique=True)
    nombre_completo = Column(String(160), nullable=False)
    correo = Column(String(160), nullable=False)
    activo = Column(Integer, nullable=False)  # BOOLEAN en SQL; mapeo como Integer para simplicidad

class MiembroEquipo(Base):
    __tablename__ = "miembros_equipo"
    id_equipo = Column(SmallInteger, ForeignKey("equipos_backoffice.id_equipo", ondelete="CASCADE"), primary_key=True)
    id_analista = Column(SmallInteger, ForeignKey("analistas.id_analista", ondelete="CASCADE"), primary_key=True)
    fecha_asignacion = Column(Date, nullable=False)
    fecha_registro = Column(TIMESTAMP)

class AsignacionReclamo(Base):
    __tablename__ = "asignaciones_reclamo"
    id_asignacion = Column(BigInteger, primary_key=True, autoincrement=True, index=True)  # BIGSERIAL
    id_reclamo = Column(BigInteger, ForeignKey("reclamos.id_reclamo", ondelete="CASCADE"), nullable=False)
    id_equipo = Column(SmallInteger, ForeignKey("equipos_backoffice.id_equipo"), nullable=False)
    id_analista = Column(SmallInteger, ForeignKey("analistas.id_analista"), nullable=False)
    fecha_asignacion = Column(Date, nullable=False)
    fecha_desasignacion = Column(Date)
    fecha_registro = Column(TIMESTAMP)