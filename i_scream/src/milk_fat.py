class MilkFat:
    value: int

    def __init__(self, value) -> None:
        if (value < 0 or 100 < value):
            raise RuntimeError
        if (isinstance(value, int) is False):
            raise RuntimeError

        self.value = value
