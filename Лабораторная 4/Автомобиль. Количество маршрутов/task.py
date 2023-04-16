from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    table_result = [[0] * m for _ in range(n)]

    def single_routes(table) -> List[List[int]]:
        for j in range(1, m):
            table[0][j] = 1
        for i in range(1, n):
            table[i][0] = 1

    if n == 1 or m == 1:
        single_routes(table_result)
        return table_result

    table_result[0][0] = 1  # значение задано для правильного расчета кол-ва маршрутов до [1][1]
    single_routes(table_result)
    for i in range(1, n):
        for j in range(1, m):
            table_result[i][j] = table_result[i - 1][j] + table_result[i][j - 1] + table_result[i - 1][j - 1]

    table_result[0][0] = 0  # точка в которой находится автомобиль не имеет маршрутов

    return table_result


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
