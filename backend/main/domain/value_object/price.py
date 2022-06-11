class Price(int):
    def __init__(self, value) -> None:
        UPPER_VALUE = 1000000
        if value < 0:
            raise ValueError

        if value > UPPER_VALUE:
            raise ValueError

        self.__value = value

    def get_value(self):
        return self.__value
