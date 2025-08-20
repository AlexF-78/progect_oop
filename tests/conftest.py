import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


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


@pytest.fixture
def sample_smartphone():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def sample_lawn_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
