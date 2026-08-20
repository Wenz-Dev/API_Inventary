# Inventario API

API REST simple para gestionar un inventario de productos. Built with FastAPI + SQLite.

## Características

- ✅ Crear productos
- ✅ Listar productos (con búsqueda por nombre)
- ✅ Obtener producto específico
- ✅ Actualizar productos
- ✅ Eliminar productos
- 🔄 Base de datos local (SQLite)

## Estructura

inventario-api/
├── database/ # Modelos + conexión BD
├── schemas/ # Validación Pydantic
├── services/ # Lógica de negocio
├── routes/ # Endpoints HTTP
└── main.py # Punto de entrada


## Instalación

### 1. Clonar el repo
\`\`\`bash
git clone https://github.com/tu-usuario/inventario-api.git
cd inventario-api
\`\`\`

### 2. Crear entorno virtual
\`\`\`bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
\`\`\`

### 3. Instalar dependencias
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Ejecutar
\`\`\`bash
python main.py
\`\`\`

## Uso

La API está en `http://localhost:8000`

Documentación interactiva: `http://localhost:8000/docs`

### Ejemplos

**Crear producto:**
\`\`\`bash
curl -X POST http://localhost:8000/productos \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Laptop", "cantidad": 5}'
\`\`\`

**Listar productos:**
\`\`\`bash
curl http://localhost:8000/productos
\`\`\`

**Buscar por nombre:**
\`\`\`bash
curl "http://localhost:8000/productos?nombre=Laptop"
\`\`\`

**Actualizar cantidad:**
\`\`\`bash
curl -X PUT http://localhost:8000/productos/1 \
  -H "Content-Type: application/json" \
  -d '{"cantidad": 10}'
\`\`\`

**Eliminar:**
\`\`\`bash
curl -X DELETE http://localhost:8000/productos/1
\`\`\`

## Próximas características

- [ ] Alertas de bajo stock
- [ ] Lista de compras
- [ ] Migrar a PostgreSQL
- [ ] Autenticación de usuarios

## Tech Stack

- Python 3.10+
- FastAPI 0.104.1
- SQLAlchemy 2.0.23
- SQLite (desarrollo), PostgreSQL (producción)

## Autor

Wenz - 2026