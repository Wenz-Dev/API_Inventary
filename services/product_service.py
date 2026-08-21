from sqlalchemy.orm import Session
from database.models import Product
from schemas.product import Add_Product, Update_Product
from fastapi import HTTPException


class ProductService:
    """Clase de servicio para manejar operaciones relacionadas con productos."""

    def __init__(self, db: Session):
        self.db = db

    # CREATE
    def add_product(self, product: Add_Product) -> Product:
        """Agrega un nuevo producto a la base de datos."""

        # Valida la logica adicional de ser necesario
        nombre_limpio = product.nombre.strip()
        if not nombre_limpio:
            raise HTTPException(
                status_code=400, detail="El nombre del producto no puede estar vacío."
            )

        # Crea un objeto en la DB
        new = Product(nombre=nombre_limpio, cantidad=product.cantidad)

        self.db.add(new)
        self.db.commit()
        self.db.refresh(new)

        return new

    # READ - obtener por id
    def get_product_by_id(self, product_id: int) -> Product:
        """Obtiene un producto por su ID."""

        product = self.db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(
                status_code=404, detail=f"Producto con ID '{product_id}' no encontrado."
            )
        return product

    # READ - obtener por nombre
    def get_product_by_name(self, nombre: str) -> Product:
        """Obtiene un producto por su nombre."""

        product = self.db.query(Product).filter(Product.nombre == nombre).first()
        if not product:
            raise HTTPException(
                status_code=404, detail=f"Producto con nombre '{nombre}' no encontrado."
            )
        return product

    # READ - todos los productos
    def all_producto(self, nombre: str = None) -> list[Product]:
        """Obtiene todos los productos, opcionalmente se puede filtrar por nombre."""

        products = self.db.query(Product).all()

        if nombre:
            # Busqueda parcial, case-insensitive
            query = query.filter(Product.nombre.ilike(f"%{nombre}%"))
        return products

    # UPDATE
    def update_product(
        self, product_id: int, update_product: Update_Product
    ) -> Product:
        """Actualiza un producto existente en la base de datos."""

        # Obtener existentes
        producto = self.get_product_by_id(product_id)

        # Actualizar solo campos enviados
        datos = update_product.dict(exclude_unset=True)

        for campo, valor in datos.items():
            # Validacion adicional si es necesario
            if campo == "nombre" and valor:
                valor = valor.strip()

            setattr(producto, campo, valor)

        self.db.commit()
        self.db.refresh(producto)

        return producto

    # DELETE
    def delete_product(self, product_id: int) -> None:
        """Elimina un producto de la base de datos."""

        product = self.get_product_by_id(product_id)

        self.db.delete(product)
        self.db.commit()
