# import pytest

from src.product import Product


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
