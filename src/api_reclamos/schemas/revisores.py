from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class RevisorBase(BaseModel):
    id_tipo_revisor: int
    nombre_completo: str
    correo: str
    activo: bool = True

class RevisorCreate(RevisorBase):
    pass

class Revisor(RevisorBase):
    id_revisor: int
    class Config:
        from_attributes = True

class RevisorReclamoBase(BaseModel):
    id_reclamo: int
    id_revisor: int
    fecha_asignacion: date
    decision: Optional[str] = None
    fecha_decision: Optional[date] = None
    nota: Optional[str] = None

class RevisorReclamoCreate(RevisorReclamoBase):
    pass

class RevisorReclamo(RevisorReclamoBase):
    id_asignacion: int
    fecha_registro: Optional[datetime] = None
    class Config:
        from_attributes = True