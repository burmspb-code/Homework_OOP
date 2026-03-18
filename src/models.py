import json
from pathlib import Path


class Product:
    """Класс для описания свойств товара.

    Attributes:
      name: str - Название товара.
      description: str - Описание товара.
      price: float - Цена товара.
      quantity: int - Количество товара в наличии.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категорий товаров.

    Attributes:
      name: str - Название категории.
      description: str - Описание товара.
      products: str - Список товаров категории.
      category_count: int - Обший счетчик категорий товаров (атрибус класса).
      product_count: int - Общий счетчик товаров.

    """

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1  # Увеличиваем счетчик категорий
        Category.product_count += len(products)  # Подсчитываем общее количество товаров


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
