from fastapi import FastAPI
from database.connection import engine, Base
from database.models import Producto
from routes.product import router

# Crear tablas automaticamente
Base.metadata.create_all(bind=engine)

# Crear APP
app = FastAPI(
    title="Inventraio API",
    description="API con arquitectura en capas + services",
    version="1.0.0",
)

# Registrar rutas
app.include_router(router)


@app.get("/")
def root():
    return {"message": "Inventario API funcionando"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
