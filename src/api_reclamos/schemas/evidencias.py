from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class EvidenciaBase(BaseModel):
    id_reclamo: int
    tipo_evidencia: str
    url_almacenamiento: Optional[str] = None
    referencia_externa: Optional[str] = None
    metadatos: Optional[str] = None
    fecha_agregado: date
    agregado_por: Optional[str] = None

class EvidenciaCreate(EvidenciaBase):
    pass

class Evidencia(EvidenciaBase):
    id_evidencia: int
    fecha_registro: Optional[datetime] = None
    class Config:
        from_attributes = True