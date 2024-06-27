from abc import (
    ABC,
    abstractmethod,
)
from typing import Iterable

from django.db.models import Q

from core.api.filters import PaginationIn
from core.apps.products.entities.products import Product as ProductEntity
from core.apps.products.exceptions.products import ProductNotFound
from core.apps.products.filters.products import ProductFilters
from core.apps.products.models.products import Product as ProductDTO


class BaseProductService(ABC):
    @abstractmethod
    def get_product_list(
        self,
        filters: ProductFilters,
        pagination: PaginationIn,
    ) -> Iterable[ProductEntity]: ...

    @abstractmethod
    def get_product_count(self, filters: ProductFilters) -> int: ...

    @abstractmethod
    def get_by_id(self, product_id: int) -> ProductEntity: ...


# TODO: закинуть фильтры в сервисный слой чтобы избежать нарушения D из SOLID
class ORMProductService(BaseProductService):
    def _build_product_query(self, filters: ProductFilters) -> Q:
        query = Q(is_visible=True)

        if filters.search is not None:
            query &= Q(title__icontains=filters.search) | Q(
                description__icontains=filters.search,
            )

        return query

    def get_product_list(
        self,
        filters: ProductFilters,
        pagination: PaginationIn,
    ) -> Iterable[ProductEntity]:
        query = self._build_product_query(filters)
        qs = ProductDTO.objects.filter(query)[
            pagination.offset:pagination.offset + pagination.limit
        ]

        return [product.to_entity() for product in qs]

    def get_product_count(self, filters: ProductFilters) -> ProductEntity:
        query = self._build_product_query(filters)

        return ProductDTO.objects.filter(query).count()

    def get_by_id(self, product_id: int) -> int:
        try:
            product_dto = ProductDTO.objects.get(pk=product_id)
        except ProductDTO.DoesNotExist:
            raise ProductNotFound(product_id=product_id)

        return product_dto.to_entity()
