class ZeroQuantityException(Exception):
    """Класс исключения при нулевом вводе количество продуктов."""
    def __init__(self, message="Товар с нулевым количеством не может быть добавлен"):
        self.message = message
