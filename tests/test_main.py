
def test_main_execution():
    """Проверяем что main.py выполняется без ошибок"""
    try:
        with open('src/main.py', 'r', encoding='utf-8') as f:
            code = f.read()
        exec(code, {'__name__': '__main__'})
        assert True
    except Exception as e:
        assert False, f"Выполнение main.py вызвало ошибку: {str(e)}"


def test_products_created():
    """Проверяем создание продуктов через анализ кода"""
    with open('src/main.py', 'r', encoding='utf-8') as f:
        code = f.read()

    # Проверяем что код содержит создание продуктов
    assert 'product1 = Product("Samsung Galaxy S23 Ultra"' in code
    assert 'product2 = Product("Iphone 15"' in code
    assert 'product3 = Product("Xiaomi Redmi Note 11"' in code


def test_categories_created():
    """Проверяем создание категорий через анализ кода"""
    with open('src/main.py', 'r', encoding='utf-8') as f:
        code = f.read()

    # Проверяем что код содержит создание категорий
    assert 'category1 = Category("Смартфоны"' in code
    assert 'category2 = Category("Телевизоры"' in code


def test_zero_quantity_product_handling():
    """Проверяем обработку товара с нулевым количеством в main.py"""
    with open('src/main.py', 'r', encoding='utf-8') as f:
        code = f.read()

    # Проверяем что код содержит обработку исключения для нулевого количества
    assert 'product_invalid = Product("Бракованный товар"' in code
    assert 'except ValueError as e:' in code
    assert 'нулевым количеством' in code


def test_middle_price_calculation():
    """Проверяем вызов метода средней цены в main.py"""
    with open('src/main.py', 'r', encoding='utf-8') as f:
        code = f.read()

    # Проверяем что код содержит вызов middle_price()
    assert 'middle_price()' in code
    assert 'category_empty.middle_price()' in code
