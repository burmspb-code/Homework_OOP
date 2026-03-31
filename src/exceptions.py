class ZeroQuantityException(Exception):
    """Класс исключения при нулевом вводе количество продуктов."""
    def __init__(self, message="Нельзя использовать нулевое количество продуктов."):
        self.message = message
