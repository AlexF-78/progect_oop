from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Обязательные атрибуты для любого продукта"""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Геттер для цены (должен быть у всех продуктов)"""
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        """Сеттер для цены (должен быть у всех продуктов)"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict):
        """Метод для создания продукта из словаря (общий для всех)"""
        pass

    @staticmethod
    @abstractmethod
    def validate_price(price: float) -> bool:
        """Проверка цены (общая для всех продуктов)"""
        pass
