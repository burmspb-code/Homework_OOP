import json

from src.load_data import load_object_from_json
from src.models import Category, Product


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
