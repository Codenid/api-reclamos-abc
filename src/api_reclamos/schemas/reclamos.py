from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class ReclamoBase(BaseModel):
    id_cliente: int
    id_producto: int
    id_tipo_reclamo: int
    id_estado_actual: int
    fecha_apertura: date
    fecha_cierre: Optional[date] = None
    canal: Optional[str] = None
    referencia_externa: str
    descripcion: Optional[str] = None
    monto: Optional[float] = None
    moneda: Optional[str] = None

class ReclamoCreate(ReclamoBase):
    pass

class Reclamo(ReclamoBase):
    id_reclamo: int
    fecha_actualizacion: Optional[datetime] = None
    class Config:
        from_attributes = True