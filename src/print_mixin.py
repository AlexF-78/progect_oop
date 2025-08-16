class PrintMixin:
    """Миксин для логирования создания объектов и вывода repr"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект класса {self.__class__.__name__} с параметрами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")

    def __repr__(self):
        """Автоматически генерирует строковое представление объекта"""
        attributes = []
        for attr, value in self.__dict__.items():
            # Обрабатываем приватные атрибуты
            if attr.startswith(f"_{self.__class__.__name__}__"):
                attr = attr.split('__')[-1]
            attributes.append(f"{attr}={repr(value)}")

        return f"{self.__class__.__name__}({', '.join(attributes)})"