# import pytest

from src.product import Product


def test_product_initialization():
    """Тест коррекции инициализации продукта"""
    product = Product("Телевизор", "4K OLED", 99999.99, 3)

    assert product.name == "Телевизор"
    assert product.description == "4K OLED"
    assert product.price == 99999.99
    assert product.quantity == 3
