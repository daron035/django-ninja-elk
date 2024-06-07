"""
1. Test products count: product count zero, product count with existing products
2. Test product returns all, w paginagion, test filters (description, title, no match)
"""

import pytest
from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilters
from core.apps.products.services.products import BaseProductService
from tests.factories.products import ProductModelFactory


@pytest.mark.django_db
def test_get_products_count_zero(product_service: BaseProductService):
    """Test product count zero with no products in database."""
    products_count = product_service.get_product_count(ProductFilters())
    assert products_count == 0, f"{products_count=}"


@pytest.mark.django_db
def test_get_products_count_exist(product_service: BaseProductService):
    """Test product count zero with no products in database."""
    expected_count = 5
    ProductModelFactory.create_batch(size=expected_count)

    products_count = product_service.get_product_count(ProductFilters())
    assert products_count == expected_count, f"{products_count=}"


@pytest.mark.django_db
def test_get_products_all(product_service: BaseProductService):
    """Test all products retrieved from database."""
    expected_count = 5
    products = ProductModelFactory.create_batch(size=expected_count)
    products_titles = {product.title for product in products}

    fetched_products = product_service.get_product_list(
        ProductFilters(),
        PaginationIn(),
    )
    fetched_titles = {product.title for product in fetched_products}

    assert len(fetched_titles) == expected_count, f"{fetched_titles=}"
    assert products_titles == fetched_titles, f"{products_titles=}"


@pytest.mark.django_db
def test_search_products(product_service: BaseProductService):
    """Test searching product names."""
    ProductModelFactory.create(title="Test Product 1")
    ProductModelFactory.create(title="Another Product")
    ProductModelFactory.create(title="Test Product 2")

    search_filter = ProductFilters(search="Test")

    fetched_products = product_service.get_product_list(search_filter, PaginationIn())
    fetched_titles = {product.title for product in fetched_products}

    expected_titles = {"Test Product 1", "Test Product 2"}

    assert len(fetched_titles) == len(expected_titles), f"{fetched_titles=}"
    assert fetched_titles == expected_titles, f"{fetched_titles=}"


@pytest.mark.django_db
def test_ping(client):
    url = "http://localhost:8000/api/ping"
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.skip(reason="not implemented")
def test_get_skip():
    assert True


@pytest.mark.xfail
def test_fail():
    assert False
