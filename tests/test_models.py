import json

from src.models import Category, Product, load_object_from_json


def test_product_creation(list_products):
    """Тест создания продуктов."""
    assert list_products[0].name == "Samsung Galaxy S23"
    assert list_products[1].name == "Iphone 15"


def test_category_creation(list_categories):
    """Тест создания категорий."""
    assert list_categories[1].name == "Budget Phones"
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_load_object_from_json(json_data, tmp_path):
    """Тест загрузки JSON файла."""
    # tmp_path - встроенная фикстура, создает временную директорию для теста
    file_path = tmp_path / "test_products.json"
    file_path.write_text(json.dumps(json_data, ensure_ascii=False), encoding="utf-8")

    categories, products = load_object_from_json(file_path)

    assert len(categories) == 1
    assert len(products) == 2
    assert categories[0].name == "Смартфоны"
    assert products[0].name == "iPhone 15"
    assert isinstance(products[1], Product)
    assert isinstance(categories[0], Category)
