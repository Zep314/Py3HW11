# Погружение в Python (семинары)
# Урок 11. ООП. Особенности Python

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
    help(mu4.MyArchive)



