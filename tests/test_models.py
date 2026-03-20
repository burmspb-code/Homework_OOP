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

def test_new_product_not_in_list(product_data_1, list_products):
    """Тест добавления нового продукта, которого нет в списке товаров."""
    new_product = Product.new_product(product_data_1, list_products)

    assert new_product.name == product_data_1["name"]
    assert new_product.price == product_data_1["price"]
    assert new_product.quantity == product_data_1["quantity"]

def test_new_category_in_list(product_data_2, list_products):
    """Тест добавления нового товара, который есть в списке товаров."""
    new_product = Product.new_product(product_data_2, list_products)

    assert new_product.price == 210000.0
    assert new_product.quantity == 18


def test_price_setter_increase(product_data_3):
    """Тест обычного повышения цены (не требует подтверждения)."""
    product_data_3.price = 210000.0
    assert product_data_3.price == 210000.0


def test_price_setter_invalid(product_data_3, capsys):
    """Тест установки отрицательной цены (не должна измениться)."""
    product_data_3.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_data_3.price == 200000.0  # Цена осталась прежней


def test_price_setter_decrease_confirm(product_data_3, monkeypatch):
    """Тест снижения цены с подтверждением 'y'."""
    # Имитируем ввод 'y' в консоль
    monkeypatch.setattr('builtins.input', lambda _: "y")

    product_data_3.price = 150000.0
    assert product_data_3.price == 150000.0


def test_price_setter_decrease_reject(product_data_3, monkeypatch):
    """Тест отмены снижения цены (ввод 'n')."""
    # Имитируем ввод 'n' в консоль
    monkeypatch.setattr('builtins.input', lambda _: "n")

    product_data_3.price = 150000.0
    assert product_data_3.price == 200000.0  # Цена не изменилась


def test_add_product():
    category = Category("Смартфоны", "Телефоны", [])
    new_product = Product("Iphone 15", "Gray", 200000.0, 10)

    category.add_product(new_product)

    # Проверяем количество товаров.
    assert len(category.products) == 1

    # Проверяем, что в первой строке есть нужное название
    assert "Iphone 15" in category.products[0]
    assert "200000.0 руб." in category.products[0]
