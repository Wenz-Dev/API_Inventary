from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database.connection import Base

class Producto(Base):
    """Modelo que representa la tabla 'productos'."""
    __tablename__= "productos"

    id = Column(Integer, primarykey=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    cantidad = Column(Integer, default=0, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.now, nullable=False)

    def __repr__(self):
        return f"<Producto(id={self.id}, nombre='{self.nombre}', cantidad={self.cantidad}, fecha_creacion={self.fecha_creacion})>"
