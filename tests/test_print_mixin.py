# import pytest
from src.print_mixin import PrintMixin


class BaseForMixinTest:
    """Базовый класс только для тестирования миксина"""

    def __init__(self, *args, **kwargs):
        pass


class MixinTestSubject(PrintMixin, BaseForMixinTest):
    """Класс для тестирования миксина """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_attr = "test_value"


def test_mixin_init_output(capsys):
    """Тест вывода при инициализации"""
    obj = MixinTestSubject("arg1", 42, key="value")
    captured = capsys.readouterr()

    assert "Создан объект класса MixinTestSubject с параметрами:" in captured.out
    assert "Позиционные аргументы: ('arg1', 42)" in captured.out
    assert "Именованные аргументы: {'key': 'value'}" in captured.out

    # Проверка, что объект корректно инициализирован
    assert hasattr(obj, 'test_attr')
    assert obj.test_attr == "test_value"


def test_mixin_repr_basic():
    """Тест базового repr"""
    obj = MixinTestSubject()
    obj.attr1 = "value1"
    assert repr(obj) == "MixinTestSubject(test_attr='test_value', attr1='value1')"


def test_mixin_repr_with_private_attrs():
    """Тест repr с приватными атрибутами"""
    obj = MixinTestSubject()
    obj._MixinTestSubject__private = "secret"
    obj.__very_private = "very_secret"
    repr_str = repr(obj)

    assert "private='secret'" in repr_str
    assert "__very_private='very_secret'" in repr_str
    assert repr_str.startswith("MixinTestSubject(")


def test_mixin_skips_internal_attrs():
    """Тест что repr пропускает служебные атрибуты"""
    obj = MixinTestSubject(1, 2, a=3)
    repr_str = repr(obj)

    assert "_init_args" not in repr_str
    assert "_init_kwargs" not in repr_str
    assert "test_attr='test_value'" in repr_str
