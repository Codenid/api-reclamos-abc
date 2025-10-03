from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.api_reclamos.deps import get_db
from src.api_reclamos.utils.pagination import pagination_params
from src.api_reclamos.models.movimientos import MovimientoReclamo
from src.api_reclamos.schemas.movimientos import MovimientoCreate, Movimiento as MovimientoSchema

router = APIRouter(prefix="/movimientos", tags=["Movimientos externos"])

@router.post("/", response_model=MovimientoSchema)
def crear_movimiento(payload: MovimientoCreate, db: Session = Depends(get_db)):
    obj = MovimientoReclamo(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/", response_model=list[MovimientoSchema])
def listar_movimientos(p: dict = Depends(pagination_params), db: Session = Depends(get_db)):
    return db.query(MovimientoReclamo).offset(p["skip"]).limit(p["limit"]).all()

@router.get("/{id_movimiento}", response_model=MovimientoSchema)
def obtener_movimiento(id_movimiento: int, db: Session = Depends(get_db)):
    obj = db.get(MovimientoReclamo, id_movimiento)
    if not obj:
        raise HTTPException(404, "Movimiento no encontrado")
    return obj

@router.delete("/{id_movimiento}")
def eliminar_movimiento(id_movimiento: int, db: Session = Depends(get_db)):
    obj = db.get(MovimientoReclamo, id_movimiento)
    if not obj:
        raise HTTPException(404, "Movimiento no encontrado")
    db.delete(obj)
    db.commit()
    return {"mensaje": "Eliminado"}