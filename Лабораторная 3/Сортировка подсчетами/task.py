from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if len(container) == 1:
        return container

    count = [0] * (max(container) + 1)
    for item in container:
        count[item] += 1

    container = []
    for index, value in enumerate(count):
        if value != 0:
            container += [index] * value
    return container
