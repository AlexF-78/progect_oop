class PrintMixin:
    """Миксин для логирования создания объектов и вывода repr"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_args = args  # Сохраняем аргументы
        self._init_kwargs = kwargs
        print(f"Создан объект класса {self.__class__.__name__} с параметрами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")

    def __repr__(self):
        """Автоматически генерирует строковое представление объекта"""
        attrs = []
        for name, value in self.__dict__.items():
            if name.startswith(f"_{self.__class__.__name__}__"):
                name = name.split('__')[-1]
            elif name in ('_init_args', '_init_kwargs'):
                continue  # Пропускаем служебные атрибуты
            attrs.append(f"{name}={repr(value)}")
        return f"{self.__class__.__name__}({', '.join(attrs)})"
