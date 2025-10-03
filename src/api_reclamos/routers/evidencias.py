from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.api_reclamos.deps import get_db
from src.api_reclamos.utils.pagination import pagination_params
from src.api_reclamos.models.evidencias import EvidenciaReclamo
from src.api_reclamos.schemas.evidencias import EvidenciaCreate, Evidencia as EvidenciaSchema

router = APIRouter(prefix="/evidencias", tags=["Evidencias"])

@router.post("/", response_model=EvidenciaSchema)
def crear_evidencia(payload: EvidenciaCreate, db: Session = Depends(get_db)):
    obj = EvidenciaReclamo(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/", response_model=list[EvidenciaSchema])
def listar_evidencias(p: dict = Depends(pagination_params), db: Session = Depends(get_db)):
    return db.query(EvidenciaReclamo).offset(p["skip"]).limit(p["limit"]).all()

@router.get("/{id_evidencia}", response_model=EvidenciaSchema)
def obtener_evidencia(id_evidencia: int, db: Session = Depends(get_db)):
    obj = db.get(EvidenciaReclamo, id_evidencia)
    if not obj:
        raise HTTPException(404, "Evidencia no encontrada")
    return obj

@router.delete("/{id_evidencia}")
def eliminar_evidencia(id_evidencia: int, db: Session = Depends(get_db)):
    obj = db.get(EvidenciaReclamo, id_evidencia)
    if not obj:
        raise HTTPException(404, "Evidencia no encontrada")
    db.delete(obj)
    db.commit()
    return {"mensaje": "Eliminado"}