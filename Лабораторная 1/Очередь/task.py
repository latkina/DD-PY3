"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Начало очереди слева, конец справа (0 1 2 3 4 ...)
        """
        self._list = []

    def enqueue(self, elem: Any) -> None:  # O(1)
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self._list.append(elem)  # O(1)

    def dequeue(self) -> Any:  # O(1)
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if not self._list:
            raise IndexError("Очередь пуста, невозможно извлечь элемент")

        return self._list.pop(0)  # O(1)

    def peek(self, ind: int = 0) -> Any:   # O(1)
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            TypeError("Некорректный тип индекса (должен быть int)")
        if not 0 <= ind < len(self._list):
            raise IndexError("Индекс вне границ очереди")

        return self._list[ind]  # O(1)

    def clear(self) -> None:
        """ Очистка очереди. """
        self._list.clear()

    def __len__(self):  # O(1)
        """ Количество элементов в очереди. """
        return len(self._list)
