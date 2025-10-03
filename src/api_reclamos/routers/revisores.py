from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.api_reclamos.deps import get_db
from src.api_reclamos.utils.pagination import pagination_params
from src.api_reclamos.models.revisores import Revisor, RevisorReclamo
from src.api_reclamos.schemas.revisores import RevisorCreate, Revisor as RevisorSchema, RevisorReclamoCreate, RevisorReclamo as RevisorReclamoSchema

router = APIRouter(prefix="/revisores", tags=["Revisores"])

@router.post("/", response_model=RevisorSchema)
def crear_revisor(payload: RevisorCreate, db: Session = Depends(get_db)):
    obj = Revisor(**payload.dict())
    obj.activo = 1 if payload.activo else 0
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/", response_model=list[RevisorSchema])
def listar_revisores(p: dict = Depends(pagination_params), db: Session = Depends(get_db)):
    return db.query(Revisor).offset(p["skip"]).limit(p["limit"]).all()

@router.post("/asignaciones", response_model=RevisorReclamoSchema)
def asignar_revisor(payload: RevisorReclamoCreate, db: Session = Depends(get_db)):
    obj = RevisorReclamo(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/asignaciones", response_model=list[RevisorReclamoSchema])
def listar_asignaciones(p: dict = Depends(pagination_params), db: Session = Depends(get_db)):
    return db.query(RevisorReclamo).offset(p["skip"]).limit(p["limit"]).all()