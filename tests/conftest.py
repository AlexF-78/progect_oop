import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_category(sample_products):
    """Фикстура для создания тестовой категории"""
    return Category("Электроника", "Техника", sample_products)


@pytest.fixture
def sample_products():
    """Фикстура для создания тестовых продуктов"""
    return [
        Product("Смартфон", "Мощный смартфон", 59999.99, 10),
        Product("Ноутбук", "Лёгкий ноутбук", 89999.99, 5),
        Product("Наушники", "Беспроводные наушники", 15999.99, 15),
    ]
