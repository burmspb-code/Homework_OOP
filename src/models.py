"""Домашняя работа 14.1"""
# атрибуты #типы_данных #создание_класса #class

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


def load_object_from_json(file_path: str | Path) -> tuple[list[Category], list[Product]]:
    """Загрузка объектов для класса Category и Product из файла JSON"""

    with open(file_path, 'r', encoding='utf-8') as file:
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
                quantity=prod.get("quantity")
            )
            products.append(product)

        category_objects.append(Category(
            name=cat.get("name"),
            description=cat.get("description"),
            products=products
        ))

        product_object.extend(products)

    return category_objects, product_object


# --- ТЕСТИРОВАНИЕ ---



# # 2. Создаем категории
#
#
# # Проверка атрибутов объектов
# assert p1.name == "Samsung Galaxy S23"
# assert cat1.name == "Smartphones"
# assert len(cat1.products) == 2
#
# # Проверка счетчиков класса
# print(f"Всего категорий: {Category.category_count}")  # Ожидаем 2
# print(f"Всего товаров: {Category.product_count}")  # Ожидаем 3
#
# assert Category.category_count == 2
# assert Category.product_count == 3
#
# print("Тесты пройдены успешно!")
#
# # Тестируем load_object_from_json
# # Подготовим временный файл
# test_data = [
#     {
#         "name": "Смартфоны",
#         "description": "Гаджеты",
#         "products": [
#             {"name": "Iphone", "description": "Apple", "price": 100.0, "quantity": 5},
#             {"name": "Samsung", "description": "Android", "price": 80.0, "quantity": 10}
#         ]
#     }
# ]

# with open('test_products.json', 'w', encoding='utf-8') as f:
#     json.dump(test_data, f)
#
# # 2. Вызываем вашу функцию
# cats, prods = load_object_from_json('test_products.json')
#
# # 3. ПРОВЕРКИ (Assertions)
# try:
#     # Проверяем количество категорий и товаров в общем списке
#     assert len(cats) == 1, "Ошибка: Должна быть 1 категория"
#     assert len(prods) == 2, "Ошибка: Должно быть 2 товара в общем списке"
#
#     # Проверяем, что внутри категории лежат объекты Product, а не словари
#     assert isinstance(cats[0].products[0], Product), "Ошибка: В категории должны быть объекты Product"
#
#     # Проверяем корректность данных первого товара
#     assert cats[0].products[0].name == "Iphone"
#     assert cats[0].products[0].price == 100.0
#
#     print("✅ Тест пройден успешно: Объекты созданы и связаны правильно!")
# except AssertionError as e:
#     print(f"❌ Тест провален: {e}")
# finally:
#     # Удаляем временный файл
#     if os.path.exists('test_products.json'):
#         os.remove('test_products.json')
