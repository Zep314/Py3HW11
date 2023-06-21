# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-
# архивов
# list-архивы также являются свойствами экземпляра

class MyArchive:
    """
    Класс для хранения значений числа и строки каждого экземпляра, созданных ранее
    с представлением данных для пользователя и программиста
    """
    numbers = []
    strings = []

    def __new__(cls, number: int, string: str):
        """
        Переопределенный метод new для сохранения ранее введенных данных
        :param number: Число для хранения 
        :param string: Строка для хранения
        """
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.strings.append(string)
        return instance

    def __init__(self, number, strings):
        """
        Сохраняем аттрибуты класса
        :param number: Число для хранения
        :param strings: Строка для хранения
        """
        self.number = number
        self.string = strings

    def __repr__(self):
        return f'MyArchive({self.number=}, {self.string=})'
