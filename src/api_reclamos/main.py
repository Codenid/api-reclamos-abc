from fastapi import FastAPI
from src.api_reclamos.routers import reclamos, catalogos, asignaciones, revisores, evidencias, movimientos
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API de Gestión de Reclamos",
    description="API basada en FastAPI para gestionar reclamos, catálogos, evidencias, asignaciones y trazabilidad.",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o lista de dominios permitidos
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusión de routers por capacidad
app.include_router(reclamos.router)
app.include_router(catalogos.router)
app.include_router(asignaciones.router)
app.include_router(revisores.router)
app.include_router(evidencias.router)
app.include_router(movimientos.router)