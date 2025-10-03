# 📘 API de Gestión de Reclamos

API basada en **FastAPI** para gestionar reclamos, catálogos, evidencias, asignaciones, revisores y trazabilidad.  
La documentación interactiva completa está disponible en:  
👉 [Swagger UI](http://54.167.30.171:8001/docs#/)

---

## 🚀 Requisitos

- Python 3.9+  
- FastAPI  
- Uvicorn  

---

## ⚙️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo

# Crear entorno virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instalar dependencias
pip install -r requirements.txt
```

---

## ▶️ Ejecución

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```

La API estará disponible en:  
- Swagger UI: [http://localhost:8001/docs](http://localhost:8001/docs)  
- Redoc: [http://localhost:8001/redoc](http://localhost:8001/redoc)  

---

## 🔑 Endpoints principales

### Reclamos
| Método | Endpoint                  | Descripción          |
|--------|---------------------------|----------------------|
| POST   | `/reclamos/`              | Crear Reclamo        |
| GET    | `/reclamos/`              | Listar Reclamos      |
| GET    | `/reclamos/{id_reclamo}`  | Obtener Reclamo      |
| PUT    | `/reclamos/{id_reclamo}`  | Actualizar Reclamo   |
| DELETE | `/reclamos/{id_reclamo}`  | Eliminar Reclamo     |

### Catálogos
| Método | Endpoint                           | Descripción             |
|--------|------------------------------------|-------------------------|
| POST   | `/catalogos/tipos-reclamo`         | Crear Tipo Reclamo      |
| GET    | `/catalogos/tipos-reclamo`         | Listar Tipos Reclamo    |
| PUT    | `/catalogos/tipos-reclamo/{id}`    | Actualizar Tipo Reclamo |
| DELETE | `/catalogos/tipos-reclamo/{id}`    | Eliminar Tipo Reclamo   |
| POST   | `/catalogos/estados-reclamo`       | Crear Estado            |
| GET    | `/catalogos/estados-reclamo`       | Listar Estados          |
| PUT    | `/catalogos/estados-reclamo/{id}`  | Actualizar Estado       |
| DELETE | `/catalogos/estados-reclamo/{id}`  | Eliminar Estado         |
| POST   | `/catalogos/tipos-revisor`         | Crear Tipo Revisor      |
| GET    | `/catalogos/tipos-revisor`         | Listar Tipos Revisor    |
| PUT    | `/catalogos/tipos-revisor/{id}`    | Actualizar Tipo Revisor |
| DELETE | `/catalogos/tipos-revisor/{id}`    | Eliminar Tipo Revisor   |

### Asignaciones y equipos
| Método | Endpoint                                | Descripción          |
|--------|-----------------------------------------|----------------------|
| POST   | `/asignaciones/historial-estados`       | Crear Historial      |
| GET    | `/asignaciones/historial-estados`       | Listar Historial     |
| POST   | `/asignaciones/equipos`                 | Crear Equipo         |
| GET    | `/asignaciones/equipos`                 | Listar Equipos       |
| POST   | `/asignaciones/analistas`               | Crear Analista       |
| GET    | `/asignaciones/analistas`               | Listar Analistas     |
| POST   | `/asignaciones/miembros-equipo`         | Crear Miembro        |
| GET    | `/asignaciones/miembros-equipo`         | Listar Miembros      |
| POST   | `/asignaciones/asignaciones-reclamo`    | Crear Asignación     |
| GET    | `/asignaciones/asignaciones-reclamo`    | Listar Asignaciones  |

### Revisores
| Método | Endpoint                      | Descripción         |
|--------|-------------------------------|---------------------|
| POST   | `/revisores/`                 | Crear Revisor       |
| GET    | `/revisores/`                 | Listar Revisores    |
| POST   | `/revisores/asignaciones`     | Asignar Revisor     |
| GET    | `/revisores/asignaciones`     | Listar Asignaciones |

### Evidencias
| Método | Endpoint                        | Descripción         |
|--------|---------------------------------|---------------------|
| POST   | `/evidencias/`                  | Crear Evidencia     |
| GET    | `/evidencias/`                  | Listar Evidencias   |
| GET    | `/evidencias/{id_evidencia}`    | Obtener Evidencia   |
| DELETE | `/evidencias/{id_evidencia}`    | Eliminar Evidencia  |

### Movimientos externos
| Método | Endpoint                           | Descripción         |
|--------|------------------------------------|---------------------|
| POST   | `/movimientos/`                    | Crear Movimiento    |
| GET    | `/movimientos/`                    | Listar Movimientos  |
| GET    | `/movimientos/{id_movimiento}`     | Obtener Movimiento  |
| DELETE | `/movimientos/{id_movimiento}`     | Eliminar Movimiento |

---

## 📋 Ejemplo de uso

```bash
curl -X POST "http://localhost:8001/reclamos/" \
     -H "Content-Type: application/json" \
     -d '{
           "titulo": "Demora en entrega",
           "descripcion": "El pedido llegó con 5 días de retraso",
           "cliente_id": 123,
           "tipo_reclamo_id": 1
         }'
```

Respuesta:

```json
{
  "id_reclamo": 1,
  "titulo": "Demora en entrega",
  "descripcion": "El pedido llegó con 5 días de retraso",
  "estado": "Abierto",
  "fecha_creacion": "2025-10-03T00:00:00"
}
```

---

## 🤝 Contribución

1. Haz un fork del proyecto  
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)  
3. Haz commit de tus cambios (`git commit -m 'Agrega nueva funcionalidad'`)  
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`)  
5. Abre un Pull Request  

---

## 📄 Licencia
Este proyecto está bajo la licencia **MIT** – consulta el archivo [LICENSE](LICENSE) para más detalles.
