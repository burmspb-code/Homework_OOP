from abc import ABC, abstractmethod
from typing import Any

from src.exceptions import ZeroQuantityException
from src.mixins import MixinLog


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех типов товаров.
    Определяет обязательный интерфейс для работы с ценой,
    складированием и операциями сложения.
    """

    @abstractmethod
    def __str__(self) -> str:
        """Выводит строковое описание объекта."""
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float:
        """Подсчет стоимости всех товаров на складе."""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, params: dict, products_list: list[Any] | None = None):
        """Логика добавления нового товара."""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Получение цены товара."""
        pass

    @price.setter
    @abstractmethod
    def price(self, price: float):
        """Установливание новой цены товара."""
        pass


class BaseEntity(ABC):
    """Абстрактный базовый класс для общих свойчт Категорий товаров и Заказов."""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self) -> str:
        """Выводит строковое описание объекта."""
        pass


class Product(MixinLog, BaseProduct):
    """Класс для описания свойств товара.

    Attributes:
      name: str - Название товара.
      description: str - Описание товара.
      __price: float - Цена товара (приватный атрибут).
      quantity: int - Количество товара в наличии.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity <= 0:
            raise ValueError
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        # Передаем аргументы дальше по цепочке MRO (в MixinLog и далее)
        super().__init__(name, description, price, quantity)

    def __str__(self):
        """Строковое описание объекта класса Product."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Подсчет стоимости всех товаров на складе."""
        if issubclass(type(other), type(self)):
            cost_self = self.quantity * self.price
            cost_other = other.quantity * other.price
            return cost_self + cost_other
        else:
            raise TypeError

    @classmethod
    def new_product(cls, params: dict, products_list: list[Any] | None = None):
        """Принимает параметры товара в словаре и возвращает созданный объект класса Product."""
        if products_list:
            for product in products_list:
                if product.name == params.get("name"):  # Если такой товар уже есть.
                    product.quantity += params.get("quantity")  # Добавляем количество.
                    product.price = max(product.price, params.get("price"))  # Берем максимальную цену.
                    return product

        return cls(**params)

    @property
    def price(self):
        """Получаем цену продукта."""
        return self.__price

    @price.setter
    def price(self, price: float):
        """Устанавливаем цену продукта."""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif price < self.__price:
            answer = input("y/n : ")
            if answer == "y":
                self.__price = price
        else:
            self.__price = price


class Category(BaseEntity):
    """Класс для представления категорий товаров.

    Attributes:
      name: str - Название категории.
      description: str - Описание товара.
      __products: str - Список товаров категории (приватный аргумент).
      category_count: int - Обший счетчик категорий товаров (атрибут класса).
      product_count: int - Общий счетчик товаров (атрибут класса).
    """

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        super().__init__(name, description)
        self.__products = products
        Category.category_count += 1  # Увеличиваем счетчик категорий
        Category.product_count += len(products)  # Подсчитываем общее количество товаров

    def __str__(self):
        """Строковое описание объекта класса Category."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product):
        """Добавление товара в список товаров."""
        try:
            if not isinstance(product, Product):
                raise TypeError("Нельзя добавить товар другого класса")
            if product.quantity == 0:
                raise ZeroQuantityException
        except (ZeroQuantityException, TypeError) as e:
            print(e)
        else:
            self.__products.append(product)
            Category.product_count += 1
            print("Товар добавлен")
        finally:
            print("Обработка добавления товара завершена")

    def get_products_list(self):
        """Возвращает список продуктов."""
        return self.__products

    @property
    def products(self):
        """Возвращает список товаров."""
        return [f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт." for prod in self.__products]

    def middle_price(self):
        """Подсчет среднего ценника на продукты в категории."""
        try:
            result = sum(product.price for product in self.__products) / len(self.__products)
            return round(result, 2)
        except ZeroDivisionError:
            print("Товар с нулевым количеством не может быть добавлен")
            return 0


class IteratorCategoryProducts:
    """Класс для итерации по товарам заданной категории."""

    def __init__(self, category: Category):
        self.category = category

    def __iter__(self):
        """Создание итератора."""
        self.value_counter = 0  # Инициализируем счетчик продуктов
        self.items = self.category.get_products_list()  # Получаем список продуктов
        return self

    def __next__(self):
        """Возвращает следующий итерируемый объект."""
        if self.value_counter < len(self.items):
            product = self.items[self.value_counter]
            self.value_counter += 1
            return product
        else:
            raise StopIteration


class OrderProduct(BaseEntity):
    """Класс для представления заказа на один товар, в котором будет ссылка на товар,
    количество купленного товара, а также итоговая стоимость.
    """

    def __init__(self, name, descriptions, product: Product, quantity: int):
        super().__init__(name, descriptions)

        # Инициализируем параметры заранее, если вдруг произойдет ошибка,
        # Защита от AttributeError при вызове метода __str__
        self.product = product
        self.quantity = 0
        self.total_price = 0

        # Если количество товаров равно 0 выбрасывается исключение ZeroQuantityException
        try:
            if quantity == 0:
                raise ZeroQuantityException
        except ZeroQuantityException as e:
            print(str(e.message))
        else:
            self.product = product  # Ссылка на товар
            self.price = product.price  # Цена товара
            self.quantity = quantity  # Количество товара
            self.total_price = product.price * quantity  # Подсчет стоимости товара
            print("Товар добавлен")
        finally:
            print("Обработка добавления товара завершена")

    def __str__(self):
        return f"Заказ '{self.name}': {self.product.name}, " f"{self.quantity} шт. Итого: {self.total_price} руб."
