from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from services.product_service import ProductService
from schemas.product import Add_Product, Update_Product, Answer_Product
from typing import List

router = APIRouter(prefix="/products", tags=["products"])


# Dependencias, inyecta servicio
def get_product_service(db: Session = Depends(get_db)) -> ProductService:
    """
    FastAPI llama autormaticamente.
    Crea una instancia de ProductService con la sesion DB.
    """
    return ProductService(db)


# CREATE
@router.post("", response_model=Answer_Product, status_code=201)
def create_product(
    product: Add_Product, service: ProductService = Depends(get_product_service)
):
    """
    Crea un producto en la base de datos.
    """
    return service.create_product(product)


# READ - Uno especifico ID
@router.get("/database/{product_id}", response_model=Answer_Product)
def get_product_by_id(
    product_id: int, service: ProductService = Depends(get_product_service)
):
    """
    Obtiene un producto de la base de datos por su ID.
    """
    return service.get_product_by_id(product_id)


# READ - Uno especifico nombre
@router.get("/database/{product_name}", response_model=Answer_Product)
def get_product_by_name(
    product_name: str, service: ProductService = Depends(get_product_service)
):
    """
    Obtiene un producto de la base de datos por su nombre
    """
    return service.get_product_by_name(product_name)


# READ-Todos
@router.get("", response_model=List[Answer_Product])
def get_all_products(
    nombre: str = None, service: ProductService = Depends(get_product_service)
):
    """
    Obtiene todos los productos de la base de datos.
    """
    return service.get_all_products(nombre)


# UPDATE
@router.put("/database/{product_id}", response_model=Answer_Product)
def update_product(
    product_id: int,
    product: Update_Product,
    service: ProductService = Depends(get_product_service),
):
    """
    Actualiza un producto en la base de datos.
    """
    return service.update_product(product_id, product)


# DELETE
@router.delete("/database/{product_id}", status_code=204)
def delete_product(
    product_id: int, service: ProductService = Depends(get_product_service)
):
    """
    Elimina un producto de la base de datos.
    Status 204: No Content, indica que la solicitud se ha procesado correctamente, pero no hay contenido que devolver.
    """
    return service.delete_product(product_id)
