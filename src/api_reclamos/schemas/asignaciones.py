from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class HistorialEstadoBase(BaseModel):
    id_reclamo: int
    id_estado_origen: Optional[int] = None
    id_estado_destino: int
    fecha_cambio: date
    usuario_cambio: Optional[str] = None
    nota: Optional[str] = None

class HistorialEstadoCreate(HistorialEstadoBase):
    pass

class HistorialEstado(HistorialEstadoBase):
    id_historial: int
    fecha_registro: Optional[datetime] = None
    class Config:
        from_attributes = True

class EquipoBackofficeBase(BaseModel):
    codigo: str
    nombre: str
    descripcion: Optional[str] = None

class EquipoBackofficeCreate(EquipoBackofficeBase):
    pass

class EquipoBackoffice(EquipoBackofficeBase):
    id_equipo: int
    class Config:
        from_attributes = True

class AnalistaBase(BaseModel):
    codigo_empleado: Optional[str] = None
    nombre_completo: str
    correo: str
    activo: bool = True

class AnalistaCreate(AnalistaBase):
    pass

class Analista(AnalistaBase):
    id_analista: int
    class Config:
        from_attributes = True

class MiembroEquipoBase(BaseModel):
    id_equipo: int
    id_analista: int
    fecha_asignacion: date

class MiembroEquipoCreate(MiembroEquipoBase):
    pass

class MiembroEquipo(MiembroEquipoBase):
    fecha_registro: Optional[datetime] = None
    class Config:
        from_attributes = True

class AsignacionReclamoBase(BaseModel):
    id_reclamo: int
    id_equipo: int
    id_analista: int
    fecha_asignacion: date
    fecha_desasignacion: Optional[date] = None

class AsignacionReclamoCreate(AsignacionReclamoBase):
    pass

class AsignacionReclamo(AsignacionReclamoBase):
    id_asignacion: int
    fecha_registro: Optional[datetime] = None
    class Config:
        from_attributes = True