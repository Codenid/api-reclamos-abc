from pydantic import BaseModel
from typing import Optional

class TipoReclamoBase(BaseModel):
    codigo: str
    nombre: str
    descripcion: Optional[str] = None

class TipoReclamoCreate(TipoReclamoBase):
    pass

class TipoReclamo(TipoReclamoBase):
    id_tipo_reclamo: int
    class Config:
        from_attributes = True

class EstadoReclamoBase(BaseModel):
    codigo: str
    nombre: str

class EstadoReclamoCreate(EstadoReclamoBase):
    pass

class EstadoReclamo(EstadoReclamoBase):
    id_estado: int
    class Config:
        from_attributes = True

class TipoRevisorBase(BaseModel):
    codigo: str
    nombre: str
    descripcion: Optional[str] = None

class TipoRevisorCreate(TipoRevisorBase):
    pass

class TipoRevisor(TipoRevisorBase):
    id_tipo_revisor: int
    class Config:
        from_attributes = True