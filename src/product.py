class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price if self.validate_price(price) else 0.0
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута price"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для приватного атрибута __price с проверкой на положительность"""
        if self.validate_price(new_price):
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")
            return

    @staticmethod
    def validate_price(price: float) -> bool:
        """Проверяем, что цена положительная"""
        return price > 0

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Создаёт и возвращает новый экземпляр класса Product из словаря."""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )
