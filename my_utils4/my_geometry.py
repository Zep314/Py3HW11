"""
Модуль содержит классы для представления геометрических фигур
"""

# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

from math import pi


class MyCircle:
    """
    Класс - окружность
    """
    def __init__(self, radius):
        self.radius = radius

    def circle_len(self) -> float:
        """
        Длина окружности
        :return:
        """
        return 2 * pi * self.radius

    def circle_square(self) -> float:
        """
        Площадь окружности
        :return:
        """
        return pi * self.radius ** 2


class MyRectangle:
    """
    Класс прямоугольник, который может быть квадратом
    """
    def __init__(self, *args):
        if len(args) == 1:  # Если один параметр - то это квадрат
            self.width = args[0]
            self.height = args[0]
        else:
            self.width = args[0]
            self.height = args[1]

    def rectangle_len(self):
        """
        Периметр прямоугольника
        :return:
        """
        return 2 * (self.height + self.width)

    def rectangle_square(self):
        """
        Площадь прямоугольника
        :return:
        """
        return self.height * self.width

    def __add__(self, other):
        """
        Сложение двух прямоугольников
        :param other:
        :return:
        """
        new_perimetr = self.rectangle_len() + other.rectangle_len()
        new_width = self.width
        new_height = new_perimetr / 2 - new_width
        return MyRectangle(new_width, new_height)

    def __sub__(self, other):
        """
        Вычитание прямоугольников
        :param other:
        :return:
        """
        new_perimetr = abs(self.rectangle_len() - other.rectangle_len())
        new_width = min(self.width, self.height, other.width, other.height)
        new_height = new_perimetr / 2 - new_width
        return MyRectangle(new_width, new_height)

    def __eq__(self, other):
        """
        Равенство двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return self.rectangle_square() == other.rectangle_square()

    def __ne__(self, other):
        """
        Неравенство двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return not self == other

    def __gt__(self, other):  # >
        """
        Сравнение двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return self.rectangle_square() > other.rectangle_square()

    def __lt__(self, other):  # <
        """
        Сравнение двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return self.rectangle_square() < other.rectangle_square()

    def __ge__(self, other):  # <=
        """
        Сравнение двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return self.rectangle_square() <= other.rectangle_square()

    def __le__(self, other):  # >=
        """
        Сравнение двух прямоугольников (сравнение по площади)
        :param other:
        :return:
        """
        return self.rectangle_square() >= other.rectangle_square()

    def __repr__(self):
        """
        Представление объекта для программистов
        :return:
        """
        return f'({self.width=}, {self.height=})'

    def __str__(self):
        """
        Представление объекта для пользователей
        :return:
        """
        return f'Прямоугольник {self.width} x {self.height}'
