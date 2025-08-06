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

    def __str__(self) -> str:
        """ Строковое представление продукта в формате: Название, цена руб. Остаток: количество шт."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Сложение продуктов (цена * количество)"""
        return (self.price * self.quantity) + (other.price * other.quantity)

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


def total_quantity(*products: Product) -> float:
    """Функция для подсчёта общей стоимости продуктов"""
    total = 0.0
    for emp in products:
        total += emp.price * emp.quantity
    return round(total, 2)

# p1 = Product("Ноутбук", "", 100000, 5) # 500000
# p2 = Product("Телефон", "", 80000, 10) # 800000
# p3 = Product("Наушники", "", 5000, 20) # 100000
#
# result = total_quantity(p1, p2, p3)
# print(result)
