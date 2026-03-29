import pytest

from src.product_classes import LawnGrass, Smartphone


def test_smartphone_creation(list_smartphones: list[Smartphone]) -> None:
    """Тест создания объектов класса Smartphones."""
    assert list_smartphones[0].name == "Samsung Galaxy S23 Ultra"
    assert list_smartphones[0].description == "256GB, Серый цвет, 200MP камера"
    assert list_smartphones[0].price == 180000.0
    assert list_smartphones[0].quantity == 5
    assert list_smartphones[0].efficiency == 95.5
    assert list_smartphones[0].model == "S23 Ultra"
    assert list_smartphones[0].memory == 256
    assert list_smartphones[0].color == "Серый"


def test_lawnGrass_creation(list_lawngrass: list[LawnGrass]) -> None:
    """Тест создания объектов класса LawnGrass."""
    assert list_lawngrass[0].name == "Газонная трава"
    assert list_lawngrass[0].description == "Элитная трава для газона"
    assert list_lawngrass[0].price == 500.0
    assert list_lawngrass[0].quantity == 20
    assert list_lawngrass[0].country == "Россия"
    assert list_lawngrass[0].germination_period == "7 дней"
    assert list_lawngrass[0].color == "Зеленый"


def test_smartphone_addition(list_smartphones: list[Smartphone]) -> None:
    """Тест сложения Smartphones одинокового класса."""
    assert list_smartphones[0] + list_smartphones[1] == 2580000


def test_smartphones_addition_error(list_smartphones: list[Smartphone]) -> None:
    """Тест сложение объекта класса Smartphone с объектом другого класса."""
    with pytest.raises(TypeError):
        list_smartphones[0] + 1


def test_lawngrass_addition(list_lawngrass: list[LawnGrass]) -> None:
    """Тест сложения LawnGrass одинокового класса."""
    assert list_lawngrass[0] + list_lawngrass[1] == 16750.0


def test_lawngrass_addition_error(list_lawngrass: list[LawnGrass]) -> None:
    """Тест сложение объекта класса LawnGrass с объектом другого класса."""
    with pytest.raises(TypeError):
        list_lawngrass[0] + 1
