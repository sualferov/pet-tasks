def daily_temperature(temperatures: list[int]) -> list[int]:
    """Определяет кол-во дней когда станет теплее."""
    """
    Пример для списка температур: [73,74,75,71,69,72,76,73]
    curr_idx = 0, temp = 73:
    1. Стек пуст. stack = [0]
    2. curr_idx = 1, temp = 74: 74 > temperatures[0] (74 > 73).
        2.1 Выталкиваем 0. Вычисляем: ans[0] = 1 - 0 = 1.
        2.2 Кладем 1. stack = [1]
    3. curr_idx = 2, temp = 75: 75 > temperatures[1] (75 > 74).
        3.2 Выталкиваем 1. Вычисляем: ans[1] = 2 - 1 = 1.
        3.2 Кладем 2. stack = [2]
    4. curr_idx = 3, temp = 71: 71 < 75. Условие while мимо.
        4.1 Кладем 3. stack = [2, 3]
    5. curr_idx = 4, temp = 69: 69 < 71. Условие while мимо.
        5.1 Кладем 4. stack = [2, 3, 4]
    6. curr_idx = 5, temp = 72:
        6.1 72 > temperatures[4] (72 > 69) -> выталкиваем 4, ans[4] = 5 - 4 = 1. stack = [2, 3]
        6.2 72 > temperatures[3] (72 > 71) -> выталкиваем 3, ans[3] = 5 - 3 = 2. stack = [2]
        6.3 72 < temperatures[2] (72 < 75) -> стоп while.
        6.4 Кладем 5. stack = [2, 5]
    """
    n = len(temperatures)
    # Инициализируем массив ответов нулями
    ans = [0] * n
    # Стек будет хранить ИНДЕКСЫ дней в монотонно убывающем порядке температур
    stack: list[int] = []

    for curr_idx, curr_temp in enumerate(temperatures):
        # Пока стек не пуст и текущая температура выше, чем у дня на вершине стека
        while stack and curr_temp > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            # Расстояние между днями — это разница их индексов
            ans[prev_idx] = curr_idx - prev_idx

        # Кладем индекс текущего дня в стек
        stack.append(curr_idx)

    return ans
