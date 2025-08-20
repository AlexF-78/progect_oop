from src.product import Product


class Category:
    name: str
    description: str
    __products: list["Product"]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []

        # Увеличиваем счётчик категорий
        Category.category_count += 1

        # Увеличиваем счётчик уникальных товаров
        Category.product_count += len(self.__products)

    def add_product(self, product):
        """
        Добавляет продукт в приватный список __products и увеличивает счётчик,
        если это экземпляр Product или его подкласса.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self) -> str:
        # Выводит название категории и количество продуктов на складе
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self) -> str:
        """Геттер возвращающий строку с информацией о всех продуктах"""
        products_info = []
        for product in self.__products:
            products_info.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")
        return "\n".join(products_info)


    def middle_price(self) -> float:
        """
        Подсчитывает средний ценник всех товаров в категории.
        Возвращает 0, если в категории нет товаров.
        """
        try:
            # Пытаемся вычислить среднюю цену
            total_price = sum(product.price for product in self.__products)
            average_price = total_price / len(self.__products)
            return round(average_price, 2)
        except ZeroDivisionError:
            # Обрабатываем случай, когда в категории нет товаров
            return 0.0
