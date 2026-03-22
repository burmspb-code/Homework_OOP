import pytest

from src.models import Category, Product


@pytest.fixture
def list_products() -> list[Product]:
    """Возвращает список тестовых товаров."""
    return [
        Product("Samsung Galaxy S23", "256GB, Gray", 95000.0, 5),
        Product("Iphone 15", "512GB, Gray", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Blue", 31000.0, 14),
    ]


@pytest.fixture
def list_categories(list_products) -> list[Category]:
    """Возвращает список тестовых категорий."""
    return [
        Category("Smartphones", "Modern communication devices", list_products[0:2]),
        Category("Budget Phones", "Affordable devices", [list_products[2]]),
    ]


@pytest.fixture
def json_data() -> list[dict]:
    """Возвращает тестовый JSON."""
    return [
        {
            "name": "Смартфоны",
            "description": "Полезные гаджеты",
            "products": [
                {
                    "name": "iPhone 15",
                    "description": "512GB",
                    "price": 100000.0,
                    "quantity": 5,
                },
                {
                    "name": "Samsung S23",
                    "description": "256GB",
                    "price": 80000.0,
                    "quantity": 10,
                },
            ],
        }
    ]


@pytest.fixture
def product_data_1() -> dict:
    """Возвращает тестовый продукт как словарь."""
    return {
        "name": "Samsung S23",
        "description": "256GB",
        "price": 80000.0,
        "quantity": 10,
    }


@pytest.fixture
def product_data_2() -> dict:
    """Возвращает тестовый продукт как словарь."""
    return {
        "name": "Iphone 15",
        "description": "512GB, Gray",
        "price": 190000.0,
        "quantity": 10,
    }


@pytest.fixture
def product_data_3() -> Product:
    """Возвращает объект класса Product."""
    return Product("Iphone 15", "Gray", 200000.0, 10)
