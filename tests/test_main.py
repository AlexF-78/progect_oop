import os

import pytest

from src.category import Category
from src.product import Product


def test_main_output(capsys):
    """Тест вывода через прямое выполнение кода"""
    # Получаем абсолютный путь к main.py
    main_path = os.path.abspath(os.path.join("src", "main.py"))

    try:
        # Читаем и выполняем код main.py
        with open(main_path, "r", encoding="utf-8") as f:
            code = compile(f.read(), main_path, "exec")
            exec(code, {"__name__": "__main__"})
    except Exception as e:
        pytest.fail(f"Ошибка выполнения main.py: {str(e)}")

    # Получаем вывод
    captured = capsys.readouterr()
    output = captured.out.strip().split('\n')

    # Проверяем ключевые элементы вывода
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in output
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in output
    assert "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт." in output

    # Проверяем, что отрицательная цена не применилась
    assert "-100" not in output


def test_main_logic():
    """Тест логики через создание объектов"""

    # Сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0

    # Создаем тестовые данные
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем категорию
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Проверяем начальное состояние
    assert Category.category_count == 1
    assert Category.product_count == 3

    # Добавляем новый продукт
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category.add_product(product4)

    # Проверяем обновлённое состояние
    assert Category.category_count == 1
    assert Category.product_count == 4

    # Проверяем создание продукта через new_product
    product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    new_product = Product.new_product(product_data)

    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5

    # Проверяем изменение цены
    new_product.price = 800
    assert new_product.price == 800


def test_product_price_validation():
    """Тест валидации цены"""
    # Создаём продукт с нормальной ценой
    product = Product("Телефон", "Смартфон", 50000, 10)

    # Сохраняем оригинальную цену
    original_price = product.price

    # 1. Проверяем, что цена не меняется при недопустимых значениях
    # тестируем отрицательную и нулевую цену
    for bad_price in [-100, 0]:
        # Пытаемся установить недопустимую цену
        product.price = bad_price
        # Цена осталась прежней
        assert product.price == original_price

    # 2. Проверяем, что цена меняется при допустимых значениях
    for good_price in [1, 100, 99999]:  # Тестируем допустимые цены
        product.price = good_price
        assert product.price == good_price  # Цена изменилась корректно


def test_main_scenario_with_fixtures(sample_category):
    """Тест сценария из main.py с использованием фикстур"""
    # Проверяем начальное состояние
    # initial_products = [p for p in sample_category.products.split("\n") if p]
    initial_total = Category.product_count

    # Добавляем новый продукт
    new_product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    sample_category.add_product(new_product)

    # Проверяем обновленное состояние
    # updated_products = [p for p in sample_category.products.split("\n") if p]
    assert Category.product_count == initial_total + 1
    assert '55" QLED 4K' in sample_category.products

    def test_main_product_addition(self):
        """Проверяем сложение продуктов """
        p1 = Product("A", "", 180000, 5)
        p2 = Product("B", "", 210000, 8)
        p3 = Product("C", "", 31000, 14)

        assert p1 + p2 == 2580000
        assert p1 + p3 == 1334000
        assert p2 + p3 == 2114000
