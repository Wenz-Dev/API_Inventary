from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Add_Product(BaseModel):
    """Esquema de datos para agregar un producto."""

    nombre: str = Field(..., min_length=1, max_length=255)
    cantidad: int = Field(default=0, ge=0)

    class Config:
        example = [{"nombre": "Leche", "cantidad": 2}]


class Update_Product(BaseModel):
    """Esquema de datos para actualizar un producto."""

    nombre: Optional[str] = Field(None, min_length=1, max_length=255)
    cantidad: Optional[int] = Field(None, ge=0)

    class Config:
        example = [{"cantidad": 2}]


class Answer_Product(BaseModel):
    """Esquema de datos para la respuesta de un producto."""

    id: int
    nombre: str
    cantidad: int
    fecha_creacion: datetime

    class Config:
        from_attributes = True
