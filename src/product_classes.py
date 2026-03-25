from src.models import Product


class Smartphone(Product):
    """Класс товаров Smartphone - наследник класса Product."""

    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str,
                 memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Сложение продуктов одинокового класса."""
        if type(other) is Smartphone:
            return (self.quantity * self.price) + (other.quantity * other.price)
        else:
            raise TypeError


class LawnGrass(Product):
    """Класс товаров LawnGrass - наследник класса Product."""

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Сложение продуктов одинокового класса."""
        if type(other) is LawnGrass:
            return (self.quantity * self.price) + (other.quantity * other.price)
        else:
            raise TypeError


if __name__ == "__main__":
    smart_1 = Smartphone("Iphone", "15", 200000.0, 10, "Gud", "6G", "1024K", "Black")
    smart_2 = Smartphone("Samsung Galaxy", "S23", 230000.0, 5, "Gud+", "5G", "1024K", "Blue")

    lawngrass_1 = LawnGrass("Газон 'Городской", "Устойчивая", 450.0, 15, "Россия", "10-14 дней", "Темно-зеленый")
    lawngrass_2 = LawnGrass("Мятлик луговой", "Плотный покров", 1250.0, 5, "Нидерланды", "21-28 дней", "Изумрудный")

    print(lawngrass_1 + lawngrass_2)
