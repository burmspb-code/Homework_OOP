# Проект CodeMarket
## Цель проекта:
### ***Раозработка ядра для интернет-магазина.***
**Инструкция по установке:**

Для работы проекта требуется [Poetry](https://python-poetry.org/).

    1. Клонируйте репозиторий:
      git clone https://github.com/burmspb-code/Homework_OOP.git
        cd project
    2. Установите зависимости:
        poetry install
    3. Запустите проект:
        poetry run python src/main

## 🧪 Тестирование:

Для проверки корректности работы модулей DataForge используется фреймворк pytest.
Тесты покрывают основные функции маскировки, фильтрации и обработки данных.

Проверяемые области
models - 

## Тестирование и покрытие
![Coverage Badge](https://img.shields.io) 

Вы можете просмотреть подробный отчет о покрытии кода тестами по ссылке:
[📊 Посмотреть Coverage Report](https://burmspb-code.github.io<Homework_OOP>/coverage/)

После запуска pytest --cov-report html подробный отчет доступен в папке htmlcov/index.html

**Используемые модули:**

    models - создание класса товаров и класса категорий для товаров.

### **Models**

Модуль содержит описание структуры данных.
