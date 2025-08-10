import pytest

from src.product import Product, total_quantity
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


def test_product_initialization():
    """Тест коррекции инициализации продукта"""
    product = Product("Телевизор", "4K OLED", 99999.99, 3)

    assert product.name == "Телевизор"
    assert product.description == "4K OLED"
    assert product.price == 99999.99
    assert product.quantity == 3


def test_price_validation():
    """Проверка только валидации цены"""
    p = Product("Тест", "Тест", 1000.0, 1)
    p.price = 1500.0
    assert p.price == 1500.0
    p.price = -500
    assert p.price == 1500.0


def test_product_str():
    """Тест строкового представления продукта"""
    product = Product("Смартфон", "Android 128GB", 59999.99, 10)

    # Проверяем формат вывода
    expected_str = "Смартфон, 59999.99 руб. Остаток: 10 шт."
    assert str(product) == expected_str

    # Проверяем с обновлёнными значениями
    product.price = 54999.99
    product.quantity = 5
    expected_str_updated = "Смартфон, 54999.99 руб. Остаток: 5 шт."
    assert str(product) == expected_str_updated


def test_product_addition():
    p1 = Product("Ноутбук", "", 100000, 2)  # 200000
    p2 = Product("Телефон", "", 80000, 3)  # 240000
    assert p1 + p2 == 440000  # 200000 + 240000


def test_total_quantity(sample_products):
    """Тест функции total_quantity"""
    p1, p2, p3 = sample_products

    # Проверяем сумму всех трёх продуктов
    assert total_quantity(p1, p2, p3) == 1289999.7

    # Проверяем сумму двух продуктов
    assert total_quantity(p1, p2) == 1049999.85

    # Проверяем с одним продуктом
    assert total_quantity(p1) == 599999.9


def test_product_addition_same_type():
    """Тест сложения товаров одного типа"""
    smartphone1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)  # 900000.0
    smartphone2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)  # 1680000.0
    assert smartphone1 + smartphone2 == 2580000.0


def test_product_addition_different_types():
    """Тест попытки сложения товаров разных типов"""
    smartphone = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    lawn_grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        smartphone + lawn_grass
