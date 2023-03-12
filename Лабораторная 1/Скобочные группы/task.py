def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок (LIFO)

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    open_bracket = []
    if not brackets_row:
        return True

    for bracket in brackets_row:
        if bracket == "(":
            open_bracket.append(bracket)
        elif bracket == ")":
            if not open_bracket:
                return False
            open_bracket.pop()
    return not open_bracket


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
