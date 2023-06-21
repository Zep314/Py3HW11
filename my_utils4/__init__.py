"""
Init-файл для пакета с моими классами для 11-ого домашнего задания
"""
from my_utils4.my_string import MyString
from my_utils4.my_archive import MyArchive
from my_utils4.my_geometry import MyRectangle
from my_utils4.my_matrix import MyMatrix
from my_utils4.my_matrix import MyMatrixSizeCreateError
from my_utils4.my_matrix import MyMatrixSizeNotMatchError

# Эти классы будем "экспортировать" для внешней работы
__all__ = ['MyString', 'MyArchive', 'MyRectangle',
           'MyMatrix', 'MyMatrixSizeCreateError', 'MyMatrixSizeNotMatchError']
