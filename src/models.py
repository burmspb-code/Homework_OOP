import json
from pathlib import Path
from typing import Any


class Product:
    """Класс для описания свойств товара.

    Attributes:
      name: str - Название товара.
      description: str - Описание товара.
      __price: float - Цена товара (приватный атрибут).
      quantity: int - Количество товара в наличии.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Строковое описание объекта класса Product."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Подсчет стоимости всех товаров на складе."""
        cost_self = self.quantity * self.price
        cost_other = other.quantity * other.price
        return cost_self + cost_other

    @classmethod
    def new_product(cls, params: dict, products_list: list[Any] | None = None):
        """Принимает параметры товара в словаре и возвращает созданный объект класса Product."""
        if products_list:
            for product in products_list:
                if product.name == params.get("name"):  # Если такой товар уже есть.
                    product.quantity += params.get("quantity")  # Добавляем количество.
                    product.price = max(
                        product.price, params.get("price")
                    )  # Берем максимальную цену.
                    return product

        return cls(**params)

    @property
    def price(self):
        """Получаем цену проукта."""
        return self.__price

    @price.setter
    def price(self, price: float):
        """Устанавливаем цену проукта."""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif price < self.__price:
            answer = input("y/n : ")
            if answer == "y":
                self.__price = price
        else:
            self.__price = price


class Category:
    """Класс для представления категорий товаров.

    Attributes:
      name: str - Название категории.
      description: str - Описание товара.
      __products: str - Список товаров категории (приватный аргумент).
      category_count: int - Обший счетчик категорий товаров (атрибус класса).
      product_count: int - Общий счетчик товаров (атрибус класса).
    """

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1  # Увеличиваем счетчик категорий
        Category.product_count += len(products)  # Подсчитываем общее количество товаров

    def __str__(self):
        """Строковое описание объекта класса Category."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product):
        """Добавление товара в список товаров."""
        self.__products.append(product)
        Category.product_count += 1

    def get_products_list(self):
        """Возвращает список продуктов."""
        return self.__products

    @property
    def products(self):
        """Возвращает список товаров."""
        return [
            f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт."
            for prod in self.__products
        ]


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


def load_object_from_json(
    file_path: str | Path,
) -> tuple[list[Category], list[Product]]:
    """Загрузка объектов для класса Category и Product из файла JSON"""

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    category_objects = []  # Создаем список для категорий
    product_object = []  # Создаем список для товаров

    for cat in data:
        products = []  # Создаем список объектов товаров для этой категории
        for prod in cat.get("products", []):
            product = Product(
                name=prod.get("name"),
                description=prod.get("description"),
                price=prod.get("price"),
                quantity=prod.get("quantity"),
            )
            products.append(product)

        category_objects.append(
            Category(
                name=cat.get("name"),
                description=cat.get("description"),
                products=products,
            )
        )

        product_object.extend(products)

    return category_objects, product_object
