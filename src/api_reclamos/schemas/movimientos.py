from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class MovimientoBase(BaseModel):
    id_reclamo: int
    id_movimiento_externo: str
    sistema_origen: str
    fecha_vinculo: date

class MovimientoCreate(MovimientoBase):
    pass

class Movimiento(MovimientoBase):
    id_movimiento: int
    fecha_registro: Optional[datetime] = None
    class Config:
        from_attributes = True