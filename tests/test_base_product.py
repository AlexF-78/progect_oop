import pytest
from abc import ABC, abstractmethod
from src.base_product import BaseProduct


class TestBaseProduct:
    """Тестируем требования абстрактного класса"""

    def test_is_abstract(self):
        """Проверяем, что класс действительно абстрактный"""
        with pytest.raises(TypeError):
            # Попытка создать экземпляр абстрактного класса должна вызывать ошибку
            BaseProduct("Test", "Desc", 100, 1)

    def test_required_methods(self):
        """Проверяем наличие обязательных методов"""
        assert hasattr(BaseProduct, '__init__')
        assert hasattr(BaseProduct, 'price')
        assert hasattr(BaseProduct.price, 'setter')
        assert hasattr(BaseProduct, 'new_product')
        assert hasattr(BaseProduct, 'validate_price')

        # Проверяем что методы абстрактные
        assert getattr(BaseProduct.__init__, '__isabstractmethod__', False)
        assert getattr(BaseProduct.price, '__isabstractmethod__', False)
