from datetime import datetime

from core.apps.products.entities.products import Product as ProductEntity
from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int  # noqa
    title: str
    description: str
    created_at: datetime
    updated_at: datetime | None = None

    @staticmethod
    def from_entity(entity: ProductEntity) -> "ProductSchema":
        return ProductSchema(
            id=entity.id,
            title=entity.description,
            description=entity.description,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


ProductListSchema = list[ProductSchema]
