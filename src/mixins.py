

class MixinLog:
    """Печатать в консоль информацию о том, от какого класса и с какими параметрами был создан объект."""

    def __init__(self, *args, **kwargs):
        super().__init__()
        print(repr(self))

    def __repr__(self):
        params_str = [f"{k}={v!r}" for k,v in self.__dict__.items()] # Создаем список строк с параметрами объекта, !r - заключает в кавычки
        return f'{self.__class__.__name__}({", ".join(params_str)})'

