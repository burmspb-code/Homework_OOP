from typing import Any

import pytest

from src.models import (
    Category,
    IteratorCategoryProducts,
    Product
)


def test_product_creation(list_products: list[Product]) -> None:
    """Тест создания продуктов."""
    assert list_products[0].name == "Samsung Galaxy S23"
    assert list_products[1].name == "Iphone 15"


def test_category_creation(list_categories: list[Category]) -> None:
    """Тест создания категорий."""
    assert list_categories[1].name == "Budget Phones"
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_new_product_not_in_list(product_data_1: dict, list_products: list[Product]) -> None:
    """Тест добавления нового продукта, которого нет в списке товаров."""
    new_product = Product.new_product(product_data_1, list_products)

    assert new_product.name == product_data_1["name"]
    assert new_product.price == product_data_1["price"]
    assert new_product.quantity == product_data_1["quantity"]


def test_new_category_in_list(product_data_2: dict, list_products: list[Product]) -> None:
    """Тест добавления нового товара, который есть в списке товаров."""
    new_product = Product.new_product(product_data_2, list_products)

    assert new_product.price == 210000.0
    assert new_product.quantity == 18


def test_price_setter_increase(product_data_3: dict) -> None:
    """Тест обычного повышения цены (не требует подтверждения)."""
    product_data_3.price = 210000.0
    assert product_data_3.price == 210000.0


def test_price_setter_invalid(product_data_3: dict, capsys) -> None:
    """Тест установки отрицательной цены (не должна измениться)."""
    product_data_3.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_data_3.price == 200000.0  # Цена осталась прежней


def test_price_setter_decrease_confirm(product_data_3: dict, monkeypatch) -> None:
    """Тест снижения цены с подтверждением 'y'."""
    # Имитируем ввод 'y' в консоль
    monkeypatch.setattr("builtins.input", lambda _: "y")

    product_data_3.price = 150000.0
    assert product_data_3.price == 150000.0


def test_price_setter_decrease_reject(product_data_3: dict, monkeypatch):
    """Тест отмены снижения цены (ввод 'n')."""
    # Имитируем ввод 'n' в консоль
    monkeypatch.setattr("builtins.input", lambda _: "n")

    product_data_3.price = 150000.0
    assert product_data_3.price == 200000.0  # Цена не изменилась


def test_add_product():
    """Тест добавления товаров."""
    category = Category("Смартфоны", "Телефоны", [])
    new_product = Product("Iphone 15", "Gray", 200000.0, 10)

    category.add_product(new_product)

    # Проверяем количество товаров.
    assert len(category.products) == 1

    # Проверяем, что в первой строке есть нужное название
    assert "Iphone 15" in category.products[0]
    assert "200000.0 руб." in category.products[0]


def test_str_product(product_data_3: dict) -> None:
    """Тест строкового представления товаров."""
    product = product_data_3
    assert str(product) == "Iphone 15, 200000.0 руб. Остаток: 10 шт."


def test_add_products(list_products: list[Product]) -> None:
    """Тест подсчета стоимости всех товаров на складе."""
    product1 = list_products[0]
    product2 = list_products[1]
    assert (product1 + product2) == 2155000


def test_str_category(list_categories: list[Category]) -> None:
    """Тест строкового представления категории."""
    category = list_categories[1]
    assert str(category) == "Budget Phones, количество продуктов: 14 шт."


def test_get_products_list(list_categories: list[Category]) -> None:
    """Тест получения списка товаров заданной категории."""
    category = list_categories[0]
    assert len(category.get_products_list()) == 2


def test_iterator_initialization(list_categories: list[Category]) -> None:
    """Тест инициализации итератора."""
    iterator = IteratorCategoryProducts(list_categories[0])
    assert iterator.category == list_categories[0]


def test_iterator_iteration(list_categories: list[Category]) -> None:
    """Тест полного цикла итерации по товарам."""
    iterator = IteratorCategoryProducts(list_categories[0])

    # Собираем все товары через цикл
    products_list = []
    for product in iterator:
        products_list.append(product)

    # Проверяем количество и типы данных
    assert len(products_list) == 2
    assert products_list[0].name == "Samsung Galaxy S23"
    assert products_list[1].name == "Iphone 15"
    # Проверяем, что это именно объекты класса Product, а не строки
    assert isinstance(products_list[0], Product)


def test_iterator_stop_iteration(list_categories: list[Category]) -> None:
    """Тест вызова исключения StopIteration по окончании товаров."""
    iterator = iter(IteratorCategoryProducts(list_categories[0]))

    # Проходим все элементы вручную
    next(iterator)
    next(iterator)

    # Следующий вызов должен вызвать StopIteration
    with pytest.raises(StopIteration):
        next(iterator)


def test_iterator_restart(list_categories: list[Category]) -> None:
    """Тест возможности повторного запуска итерации."""
    iterator = IteratorCategoryProducts(list_categories[0])

    first_run = list(iterator)
    second_run = list(iterator)  # __iter__ сбросит счетчик

    assert len(first_run) == len(second_run) == 2

def test_category_addition_error(list_products: list[Product]) -> None:
    """Тест возбуждения ошибки при сложении объектов разных классов."""
    with pytest.raises(TypeError):
        list_products[0] + 1

def test_category_add_product_error(list_categories: list[Category]) -> None:
    """Тест возбуждения ошибки при добавлении объекта другого класса в категорию товаров."""
    wrong_product: Any = 1
    with pytest.raises(TypeError):
        list_categories[0].add_product(wrong_product)
