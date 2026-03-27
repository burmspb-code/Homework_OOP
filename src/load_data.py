import json
from pathlib import Path

from src.models import Category, Product


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
