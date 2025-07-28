import os

import pytest


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
    output = captured.out

    # Проверяем ключевые элементы вывода
    assert "Samsung Galaxy S23 Ultra" in output
    assert "256GB, Серый цвет, 200MP камера" in output
    assert "180000.0" in output
    assert "Смартфоны" in output
    assert "Телевизоры" in output


def test_main_logic():
    """Тест логики через создание объектов"""
    from src.category import Category
    from src.product import Product

    # Сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0

    # Создаем тестовые данные
    p1 = Product("Тест1", "Описание1", 1000, 1)
    p2 = Product("Тест2", "Описание2", 2000, 2)
    # Создаем категорию
    cat = Category("Электроника", "Техника", [p1, p2])

    # Проверяем состояние
    assert Category.category_count == 1
    assert Category.product_count == 2

    # Проверяем атрибуты
    assert cat.name == "Электроника"
    assert len(cat.products) == 2
