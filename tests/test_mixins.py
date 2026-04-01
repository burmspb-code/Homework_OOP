from src.models import Product
from src.product_classes import LawnGrass, Smartphone


def test_MixinLog_create(capsys) -> None:
    """Тест вывода лога в консоль."""

    # Для класса Product
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr().out.strip()  # Выбераем только поле out и удаляем лишние переносы/пробелы
    assert (
        message == "Product(name='Samsung Galaxy S23 Ultra', description='256GB, "
        "Серый цвет, 200MP камера', _Product__price=180000.0, quantity=5)"
    )

    # Для класса Smartphone
    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr().out.strip()
    assert (
        message == "Smartphone(efficiency=98.2, model='15', memory=512, color='Gray space', name='Iphone 15', "
        "description='512GB, Gray space', _Product__price=210000.0, quantity=8)"
    )

    # Для класса
    LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
    message = capsys.readouterr().out.strip()
    assert (
        message
        == "LawnGrass(country='США', germination_period='5 дней', color='Темно-зеленый', name='Газонная трава 2', "
        "description='Выносливая трава', _Product__price=450.0, quantity=15)"
    )
