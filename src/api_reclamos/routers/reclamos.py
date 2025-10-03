from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.api_reclamos.deps import get_db
from src.api_reclamos.utils.pagination import pagination_params
from src.api_reclamos.models.reclamos import Reclamo
from src.api_reclamos.schemas.reclamos import ReclamoCreate, Reclamo as ReclamoSchema

router = APIRouter(prefix="/reclamos", tags=["Reclamos"])

@router.post("/", response_model=ReclamoSchema)
def crear_reclamo(payload: ReclamoCreate, db: Session = Depends(get_db)):
    obj = Reclamo(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/", response_model=list[ReclamoSchema])
def listar_reclamos(p: dict = Depends(pagination_params), db: Session = Depends(get_db)):
    return db.query(Reclamo).offset(p["skip"]).limit(p["limit"]).all()

@router.get("/{id_reclamo}", response_model=ReclamoSchema)
def obtener_reclamo(id_reclamo: int, db: Session = Depends(get_db)):
    obj = db.get(Reclamo, id_reclamo)
    if not obj:
        raise HTTPException(404, "Reclamo no encontrado")
    return obj

@router.put("/{id_reclamo}", response_model=ReclamoSchema)
def actualizar_reclamo(id_reclamo: int, payload: ReclamoCreate, db: Session = Depends(get_db)):
    obj = db.get(Reclamo, id_reclamo)
    if not obj:
        raise HTTPException(404, "Reclamo no encontrado")
    for k, v in payload.dict().items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj

@router.delete("/{id_reclamo}")
def eliminar_reclamo(id_reclamo: int, db: Session = Depends(get_db)):
    obj = db.get(Reclamo, id_reclamo)
    if not obj:
        raise HTTPException(404, "Reclamo no encontrado")
    db.delete(obj)
    db.commit()
    return {"mensaje": "Eliminado"}