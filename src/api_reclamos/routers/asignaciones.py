from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api_reclamos.deps import get_db
from src.api_reclamos.utils.pagination import pagination_params

# Importa modelos (SQLAlchemy) con alias
from src.api_reclamos.models.asignaciones import (
    HistorialEstado as HistorialEstadoModel,
    EquipoBackoffice as EquipoBackofficeModel,
    Analista as AnalistaModel,
    MiembroEquipo as MiembroEquipoModel,
    AsignacionReclamo as AsignacionReclamoModel,
)

# Importa schemas (Pydantic) con alias
from src.api_reclamos.schemas.asignaciones import (
    HistorialEstadoCreate, HistorialEstado as HistorialEstadoSchema,
    EquipoBackofficeCreate, EquipoBackoffice as EquipoBackofficeSchema,
    AnalistaCreate, Analista as AnalistaSchema,
    MiembroEquipoCreate, MiembroEquipo as MiembroEquipoSchema,
    AsignacionReclamoCreate, AsignacionReclamo as AsignacionReclamoSchema,
)

router = APIRouter(prefix="/asignaciones", tags=["Asignaciones y equipos"])

# ---------------------------
# Historial de estados
# ---------------------------
@router.post("/historial-estados", response_model=HistorialEstadoSchema)
def crear_historial(payload: HistorialEstadoCreate, db: Session = Depends(get_db)):
    obj = HistorialEstadoModel(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/historial-estados", response_model=list[HistorialEstadoSchema])
def listar_historial(p: dict = Depends(pagination_params), db: Session = Depends(get_db)):
    return db.query(HistorialEstadoModel).offset(p["skip"]).limit(p["limit"]).all()

# ---------------------------
# Equipos
# ---------------------------
@router.post("/equipos", response_model=EquipoBackofficeSchema)
def crear_equipo(payload: EquipoBackofficeCreate, db: Session = Depends(get_db)):
    obj = EquipoBackofficeModel(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/equipos", response_model=list[EquipoBackofficeSchema])
def listar_equipos(p: dict = Depends(pagination_params), db: Session = Depends(get_db)):
    return db.query(EquipoBackofficeModel).offset(p["skip"]).limit(p["limit"]).all()

# ---------------------------
# Analistas
# ---------------------------
@router.post("/analistas", response_model=AnalistaSchema)
def crear_analista(payload: AnalistaCreate, db: Session = Depends(get_db)):
    obj = AnalistaModel(**payload.dict())
    obj.activo = 1 if payload.activo else 0
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/analistas", response_model=list[AnalistaSchema])
def listar_analistas(p: dict = Depends(pagination_params), db: Session = Depends(get_db)):
    return db.query(AnalistaModel).offset(p["skip"]).limit(p["limit"]).all()

# ---------------------------
# Miembros de equipo
# ---------------------------
@router.post("/miembros-equipo", response_model=MiembroEquipoSchema)
def crear_miembro(payload: MiembroEquipoCreate, db: Session = Depends(get_db)):
    obj = MiembroEquipoModel(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/miembros-equipo", response_model=list[MiembroEquipoSchema])
def listar_miembros(p: dict = Depends(pagination_params), db: Session = Depends(get_db)):
    return db.query(MiembroEquipoModel).offset(p["skip"]).limit(p["limit"]).all()

# ---------------------------
# Asignaciones de reclamo
# ---------------------------
@router.post("/asignaciones-reclamo", response_model=AsignacionReclamoSchema)
def crear_asignacion(payload: AsignacionReclamoCreate, db: Session = Depends(get_db)):
    obj = AsignacionReclamoModel(**payload.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/asignaciones-reclamo", response_model=list[AsignacionReclamoSchema])
def listar_asignaciones(p: dict = Depends(pagination_params), db: Session = Depends(get_db)):
    return db.query(AsignacionReclamoModel).offset(p["skip"]).limit(p["limit"]).all()