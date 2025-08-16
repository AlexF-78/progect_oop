import pytest
from src.print_mixin import PrintMixin


def test_mixin_output(capsys):
    """Тестируем вывод при создании объекта"""

    class TestProduct(PrintMixin):
        def __init__(self, name, price):
            self.name = name
            self.price = price

    # Создаём объект
    TestProduct("Телевизор", 10000)

    # Проверяем вывод
    captured = capsys.readouterr()
    assert "Создан объект класса TestProduct" in captured.out
    assert "Телевизор" in captured.out or "10000" in captured.out


def test_repr_output():
    """Тестируем строковое представление"""

    class TestProduct(PrintMixin):
        def __init__(self, id):
            self.id = id

    obj = TestProduct(123)
    assert "123" in repr(obj)import pytest
from src.print_mixin import PrintMixin

def test_mixin_output(capsys):
    """Тестируем вывод при создании объекта"""
    class TestProduct(PrintMixin):
        def __init__(self, name, price):
            self.name = name
            self.price = price
    
    # Создаём объект
    TestProduct("Телевизор", 10000)
    
    # Проверяем вывод
    captured = capsys.readouterr()
    assert "Создан объект класса TestProduct" in captured.out
    assert "Телевизор" in captured.out or "10000" in captured.out

def test_repr_output():
    """Тестируем строковое представление"""
    class TestProduct(PrintMixin):
        def __init__(self, id):
            self.id = id
    
    obj = TestProduct(123)
    assert "123" in repr(obj)
