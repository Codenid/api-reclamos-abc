from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api_reclamos.deps import get_db
from src.api_reclamos.utils.pagination import pagination_params

# Importa modelos (SQLAlchemy)
from src.api_reclamos.models.catalogos import (
    TipoReclamo as TipoReclamoModel,
    EstadoReclamo as EstadoReclamoModel,
    TipoRevisor as TipoRevisorModel,
)

# Importa schemas (Pydantic)
from src.api_reclamos.schemas.catalogos import (
    TipoReclamoCreate, TipoReclamo as TipoReclamoSchema,
    EstadoReclamoCreate, EstadoReclamo as EstadoReclamoSchema,
    TipoRevisorCreate, TipoRevisor as TipoRevisorSchema,
)

router = APIRouter(prefix="/catalogos", tags=["Catálogos"])

# ---------------------------
# Tipos de reclamo
# ---------------------------
@router.post("/tipos-reclamo", response_model=TipoReclamoSchema)
def crear_tipo_reclamo(payload: TipoReclamoCreate, db: Session = Depends(get_db)):
    obj = TipoReclamoModel(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/tipos-reclamo", response_model=list[TipoReclamoSchema])
def listar_tipos_reclamo(p: dict = Depends(pagination_params), db: Session = Depends(get_db)):
    return db.query(TipoReclamoModel).offset(p["skip"]).limit(p["limit"]).all()

@router.put("/tipos-reclamo/{id}", response_model=TipoReclamoSchema)
def actualizar_tipo_reclamo(id: int, payload: TipoReclamoCreate, db: Session = Depends(get_db)):
    obj = db.get(TipoReclamoModel, id)
    if not obj:
        raise HTTPException(404, "Tipo de reclamo no encontrado")
    for k, v in payload.dict().items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj

@router.delete("/tipos-reclamo/{id}")
def eliminar_tipo_reclamo(id: int, db: Session = Depends(get_db)):
    obj = db.get(TipoReclamoModel, id)
    if not obj:
        raise HTTPException(404, "Tipo de reclamo no encontrado")
    db.delete(obj)
    db.commit()
    return {"mensaje": "Eliminado"}

# ---------------------------
# Estados de reclamo
# ---------------------------
@router.post("/estados-reclamo", response_model=EstadoReclamoSchema)
def crear_estado(payload: EstadoReclamoCreate, db: Session = Depends(get_db)):
    obj = EstadoReclamoModel(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/estados-reclamo", response_model=list[EstadoReclamoSchema])
def listar_estados(p: dict = Depends(pagination_params), db: Session = Depends(get_db)):
    return db.query(EstadoReclamoModel).offset(p["skip"]).limit(p["limit"]).all()

@router.put("/estados-reclamo/{id}", response_model=EstadoReclamoSchema)
def actualizar_estado(id: int, payload: EstadoReclamoCreate, db: Session = Depends(get_db)):
    obj = db.get(EstadoReclamoModel, id)
    if not obj:
        raise HTTPException(404, "Estado no encontrado")
    for k, v in payload.dict().items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj

@router.delete("/estados-reclamo/{id}")
def eliminar_estado(id: int, db: Session = Depends(get_db)):
    obj = db.get(EstadoReclamoModel, id)
    if not obj:
        raise HTTPException(404, "Estado no encontrado")
    db.delete(obj)
    db.commit()
    return {"mensaje": "Eliminado"}

# ---------------------------
# Tipos de revisor
# ---------------------------
@router.post("/tipos-revisor", response_model=TipoRevisorSchema)
def crear_tipo_revisor(payload: TipoRevisorCreate, db: Session = Depends(get_db)):
    obj = TipoRevisorModel(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/tipos-revisor", response_model=list[TipoRevisorSchema])
def listar_tipos_revisor(p: dict = Depends(pagination_params), db: Session = Depends(get_db)):
    return db.query(TipoRevisorModel).offset(p["skip"]).limit(p["limit"]).all()

@router.put("/tipos-revisor/{id}", response_model=TipoRevisorSchema)
def actualizar_tipo_revisor(id: int, payload: TipoRevisorCreate, db: Session = Depends(get_db)):
    obj = db.get(TipoRevisorModel, id)
    if not obj:
        raise HTTPException(404, "Tipo de revisor no encontrado")
    for k, v in payload.dict().items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj

@router.delete("/tipos-revisor/{id}")
def eliminar_tipo_revisor(id: int, db: Session = Depends(get_db)):
    obj = db.get(TipoRevisorModel, id)
    if not obj:
        raise HTTPException(404, "Tipo de revisor no encontrado")
    db.delete(obj)
    db.commit()
    return {"mensaje": "Eliminado"}