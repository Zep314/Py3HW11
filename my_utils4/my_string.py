"""
Модуль содержит класс - строку с расширенными методами и аттрибутами
"""

# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

# Добавьте к задачам 1 и 2 строки документации для классов.

import time


class MyString(str):
    """
    Расширенный класс str
    """

    def __new__(cls, value: str, author: str = ''):
        """
        Расширенный метод new с параметрами автора и времени создания
        :param value: Сама строка
        :param author: Имя автора
        """
        instance = super().__new__(cls, value)
        instance.author = author
        instance.date_time = time.strftime("%Y.%m.%d %H:%M:%S", time.gmtime(time.time()))
        return instance

    def __repr__(self):
        """
        Выводим на печать представление для программистов
        :return:
        """
        return f'{self}, {self.author=}, {self.date_time=}'
