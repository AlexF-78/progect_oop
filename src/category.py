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
        """Добавляет в приватный список __products и увеличивает счётчик"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер возвращающий строку с информацией о всех продуктах"""
        products_info = []
        for product in self.__products:
            products_info.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")
        return "\n".join(products_info)
