# import pytest
from src.category import Category


def test_category_initialization(sample_category, sample_products):
    """Тест корректности инициализации категории"""
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Техника"
    assert len(sample_category.products) == 3
    assert sample_category.products == sample_products


def test_category_counters(sample_products):
    """Тест подсчета количества категорий и уникальных продуктов"""
    # Сбрасываем счетчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    # Создаем первую категорию (2 продукта)
    cat1 = Category("Категория 1", "Описание 1", sample_products[:2])
    assert Category.category_count == 1
    assert Category.product_count == 2
    assert len(cat1.products) == 2

    # Создаем вторую категорию (1 продукт)
    cat2 = Category("Категория 2", "Описание 2", [sample_products[2]])
    assert Category.category_count == 2
    assert Category.product_count == 3
    assert len(cat2.products) == 1


def test_empty_category():
    """Тест создания категории без продуктов"""
    # Сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0

    empty_cat = Category("Пустая", "Нет товаров", [])

    assert Category.category_count == 1
    assert Category.product_count == 0
    assert len(empty_cat.products) == 0
