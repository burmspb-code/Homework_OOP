from src.mixins import MixinLog
from src.models import Product


class Smartphone(Product):
    """Класс товаров Smartphone - наследник класса Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):

        # Сначала сохраняем уникальные данные
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

        # Потом вызываем родителя, для правильной логики работы Mixin
        super().__init__(name, description, price, quantity)

    def __add__(self, other) -> float:
        """Сложение продуктов одинокового класса."""
        if type(other) is Smartphone:
            return (self.quantity * self.price) + (other.quantity * other.price)
        else:
            raise TypeError


class LawnGrass(Product):
    """Класс товаров LawnGrass - наследник класса Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):

        # Сначала сохраняем уникальные данные
        self.country = country
        self.germination_period = germination_period
        self.color = color

        # Потом вызываем родителя, для правильной логики работы Mixin
        super().__init__(name, description, price, quantity)

    def __add__(self, other) -> float:
        """Сложение продуктов одинокового класса."""
        if type(other) is LawnGrass:
            return (self.quantity * self.price) + (other.quantity * other.price)
        else:
            raise TypeError
