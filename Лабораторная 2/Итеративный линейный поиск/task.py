"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    min_value = arr[0]
    index = 0

    for value_index in range(len(arr)):
        if min_value > arr[value_index]:
            min_value = arr[value_index]
            index = value_index

    return index
