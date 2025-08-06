# import pytest
from src.category import Category
from src.product import Product


def test_category_initialization(sample_category, sample_products):
    """Тест корректности инициализации категории"""
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Техника"
    # assert len(sample_category.products) == 3
    # assert sample_category.products == sample_products
    assert "Смартфон, 59999.99 руб. Остаток: 10 шт." in sample_category.products


def test_category_counters(sample_products):
    """Тест подсчета количества категорий и уникальных продуктов"""

    # Сбрасываем счетчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    # Создаем первую категорию (2 продукта)
    cat1 = Category("Категория 1", "Описание 1", sample_products[:2])
    assert Category.category_count == 1
    assert Category.product_count == 2
    # assert len(cat1.products) == 2
    assert "\n" in cat1.products

    # Создаем вторую категорию (1 продукт)
    cat2 = Category("Категория 2", "Описание 2", [sample_products[2]])
    assert Category.category_count == 2
    assert Category.product_count == 3
    # assert len(cat2.products) == 1
    assert "Наушники" in cat2.products


def test_empty_category():
    """Тест создания категории без продуктов"""
    # Сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0

    empty_cat = Category("Пустая", "Нет товаров", [])

    assert Category.category_count == 1
    assert Category.product_count == 0
    assert len(empty_cat.products) == 0


def test_add_product(sample_category):
    """Проверка добавления одного продукта"""
    # Получаем список строк продуктов (разделяем по \n и убираем пустые строки)
    initial_products = [p for p in sample_category.products.split('\n') if p]
    initial_count = len(initial_products)
    initial_total = Category.product_count

    new_product = Product("Планшет", "Новый", 30000.0, 5)
    sample_category.add_product(new_product)

    # Проверяем, что продукт добавился
    assert "Планшет, 30000.0 руб. Остаток: 5 шт." in sample_category.products

    # Получаем обновленный список продуктов
    updated_products = [p for p in sample_category.products.split('\n') if p]
    assert len(updated_products) == initial_count + 1
    assert Category.product_count == initial_total + 1


def test_category_str_representation(sample_category, sample_products):
    """Тест строкового представления категории (метод __str__)"""
    # Проверяем для категории с продуктами
    expected_str = "Электроника, количество продуктов: 30 шт."  # 10 (Смартфон) + 5 (Ноутбук) + 15 (Наушники)
    assert str(sample_category) == expected_str

    # Проверяем для пустой категории
    empty_category = Category("Пустая", "Нет товаров", [])
    assert str(empty_category) == "Пустая, количество продуктов: 0 шт."

    # Проверяем после добавления продукта
    new_product = Product("Планшет", "Новый", 30000.0, 7)
    sample_category.add_product(new_product)
    assert str(sample_category) == "Электроника, количество продуктов: 37 шт."
