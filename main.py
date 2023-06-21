# Погружение в Python (семинары)
# Урок 11. ООП. Особенности Python

# Создайте класс Матрица. Добавьте методы для:
# вывода на печать,
# сравнения,
# сложения,
# *умножения матриц


import my_utils4 as mu4

if __name__ == '__main__':
    print('--== Тестирование класса MyString ==--')
    my_string = mu4.MyString('Привет!', 'Марк Лутц')
    print(f'{my_string=}')
    print(f'{my_string.author=}')
    print(f'{my_string.date_time=}')
    print(f'{my_string.lower()=}')

    print('\n--== Тестирование класса MyArchive ==--')
    my_archive1 = mu4.MyArchive(1, 'Один')
    my_archive2 = mu4.MyArchive(2, 'Два')
    print(f'{my_archive1.numbers=} {my_archive1.strings=}')
    print(f'{my_archive2.numbers=} {my_archive2.strings=}')
    my_archive3 = mu4.MyArchive(3, 'Три')
    print(f'{my_archive3.numbers=} {my_archive3.strings=}')

    #    help(mu4.MyString)
    #    help(mu4.MyArchive)

    print('Тестируем метод __repr__:')
    print(f'{my_archive3=}')
    print('Тестируем метод __str__:')
    print(f'{my_archive3}')

    print('\n--== Тестирование класса MyRectangle ==--')
    rectangle1 = mu4.MyRectangle(5, 4)
    rectangle2 = mu4.MyRectangle(12, 10)
    rectangle3 = rectangle1 + rectangle2
    print(f'Периметр прямоугольника1 {rectangle1.width}x{rectangle1.height} равна {rectangle1.rectangle_len()=}')
    print(f'Площадь прямоугольника1 {rectangle1.width}x{rectangle1.height} равна {rectangle1.rectangle_square()=}')
    print(f'Периметр прямоугольника2 {rectangle2.width}x{rectangle2.height} равна {rectangle2.rectangle_len()=}')
    print(f'Площадь прямоугольника2 {rectangle2.width}x{rectangle2.height} равна {rectangle2.rectangle_square()=}')
    print(f'Периметр прямоугольника3 {rectangle3.width}x{rectangle3.height} равна {rectangle3.rectangle_len()=}')
    print(f'Площадь прямоугольника3 {rectangle3.width}x{rectangle3.height} равна {rectangle3.rectangle_square()=}')

    rectangle4 = rectangle1 - rectangle2

    print(f'Периметр прямоугольника4 {rectangle4.width}x{rectangle4.height} равна {rectangle4.rectangle_len()=}')
    print(f'Площадь прямоугольника4 {rectangle4.width}x{rectangle4.height} равна {rectangle4.rectangle_square()=}')
    print(f'Прямоугольник rectangle1 {"" if rectangle1 == rectangle2 else "не "}равен прямоугольнику rectangle2')
    print(f'Прямоугольник rectangle1 {"" if rectangle1 == rectangle1 else "не "}равен прямоугольнику rectangle1')
    print(f'Прямоугольник rectangle1 {"больше" if rectangle1 > rectangle2 else "меньше"} прямоугольника rectangle2')
    print(rectangle1)
    print(f'{rectangle1=}')

    print('\n--== ДОМАШНЕЕ ЗАДАНИЕ!!!! ==--')
    print('\n--== Тестирование класса MyMatrix ==--')
    matrix1 = mu4.MyMatrix([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])
    try:
        matrix2 = mu4.MyMatrix([[11, 12, 13, 20],
                                [14, 15, 16],
                                [17, 18, 19]])
    except mu4.MyMatrixSizeCreateError:
        print('Ошибка создания матрицы! Количество чисел в во всех строках должно быть равно!')

    matrix2 = mu4.MyMatrix([[11, 12, 13],
                            [14, 15, 16],
                            [17, 18, 19]])

    print(f'{matrix2.get_width()=}')
    print(f'{matrix2.get_height()=}')
    print(f'{matrix2=}')
    print('Матрица matrix1:')
    print(f'{matrix1}')
    print('Матрица matrix2:')
    print(f'{matrix2}')

    try:
        matrix3 = matrix1 + matrix2
        print('Матрица matrix3 (matrix1 + matrix2):')
        print(f'{matrix3}')
    except mu4.MyMatrixSizeNotMatchError:
        print('Неверные размеры складываемых матриц!')

    print(f'Матрица matrix1 {"" if matrix1 == matrix2 else "не "}равна матрице matrix2')
    print(f'Матрица matrix1 {"" if matrix1 == matrix1 else "не "}равна матрице matrix1')

    print(f'Матрица matrix1 {"больше" if matrix1 > matrix2 else "меньше"} матрицы matrix2')

    print('\nУмножение матриц')
    matrix_a = mu4.MyMatrix([[1, 1, 0],
                            [1, 0, 2]])
    matrix_b = mu4.MyMatrix([[1, 0, 2, 1],
                            [2, 1, 2, 0],
                            [1, 1, 0, 3]])
    print('Матрица matrix_a:')
    print(f'{matrix_a}')
    print('Матрица matrix_b:')
    print(f'{matrix_b}')

    try:
        matrix_c = matrix_a * matrix_b
        print('Матрица matrix_c (matrix1 * matrix2):')
        print(f'{matrix_c}')
    except mu4.MyMatrixSizeNotMatchError:
        print('Неверные размеры перемножаемых матриц!')

# Результат работы:
# C:\Work\python\dz3\Py3HW11\venv\Scripts\python.exe C:/Work/python/dz3/Py3HW11/main.py
# --== Тестирование класса MyString ==--
# my_string=Привет!, self.author='Марк Лутц', self.date_time='2023.06.21 13:20:19'
# my_string.author='Марк Лутц'
# my_string.date_time='2023.06.21 13:20:19'
# my_string.lower()='привет!'
#
# --== Тестирование класса MyArchive ==--
# my_archive1.numbers=[1, 2] my_archive1.strings=['Один', 'Два']
# my_archive2.numbers=[1, 2] my_archive2.strings=['Один', 'Два']
# my_archive3.numbers=[1, 2, 3] my_archive3.strings=['Один', 'Два', 'Три']
# Тестируем метод __repr__:
# my_archive3=MyArchive(self.number=3, self.string='Три')
# Тестируем метод __str__:
# Число: 3, Строка: 'Три'
#
# --== Тестирование класса MyRectangle ==--
# Периметр прямоугольника1 5x4 равна rectangle1.rectangle_len()=18
# Площадь прямоугольника1 5x4 равна rectangle1.rectangle_square()=20
# Периметр прямоугольника2 12x10 равна rectangle2.rectangle_len()=44
# Площадь прямоугольника2 12x10 равна rectangle2.rectangle_square()=120
# Периметр прямоугольника3 5x26.0 равна rectangle3.rectangle_len()=62.0
# Площадь прямоугольника3 5x26.0 равна rectangle3.rectangle_square()=130.0
# Периметр прямоугольника4 4x9.0 равна rectangle4.rectangle_len()=26.0
# Площадь прямоугольника4 4x9.0 равна rectangle4.rectangle_square()=36.0
# Прямоугольник rectangle1 не равен прямоугольнику rectangle2
# Прямоугольник rectangle1 равен прямоугольнику rectangle1
# Прямоугольник rectangle1 меньше прямоугольника rectangle2
# Прямоугольник 5 x 4
# rectangle1=(self.width=5, self.height=4)
#
# --== ДОМАШНЕЕ ЗАДАНИЕ!!!! ==--
#
# --== Тестирование класса MyMatrix ==--
# Ошибка создания матрицы! Количество чисел в во всех строках должно быть равно!
# matrix2.get_width()=3
# matrix2.get_height()=3
# matrix2=[[11, 12, 13], [14, 15, 16], [17, 18, 19]]
# Матрица matrix1:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
#
# Матрица matrix2:
# [11, 12, 13]
# [14, 15, 16]
# [17, 18, 19]
#
# Матрица matrix3 (matrix1 + matrix2):
# [12, 14, 16]
# [18, 20, 22]
# [24, 26, 28]
#
# Матрица matrix1 не равна матрице matrix2
# Матрица matrix1 равна матрице matrix1
# Матрица matrix1 меньше матрицы matrix2
#
# Умножение матриц
# Матрица matrix_a:
# [1, 1, 0]
# [1, 0, 2]
#
# Матрица matrix_b:
# [1, 0, 2, 1]
# [2, 1, 2, 0]
# [1, 1, 0, 3]
#
# Матрица matrix_c (matrix1 * matrix2):
# [3, 1, 4, 1]
# [3, 2, 2, 7]
#
#
# Process finished with exit code 0
