def next_greater_element_1(nums1: list[int], nums2: list[int]) -> list[int]:
    """Возвращает первый больший элемент из списка 2 для каждого элемента списка 1."""
    """
    Пример работы стека для nums2 = [1, 3, 4, 2]
    1. num = 1: Стек пуст. stack = [1]
    2. num = 3: 3 > stack[-1] (3 > 1). Выталкиваем 1. Записываем в словарь {1: 3}. Кладем 3. stack = [3]
    3. num = 4: 4 > stack[-1] (4 > 3). Выталкиваем 3. Записываем в словарь {3: 4}. Кладем 4. stack = [4]
    4. num = 2: 2 < stack[-1] (2 < 4). Условие while не выполнено. Кладем 2. stack = [4, 2]
    Итог словаря next_greater: {1: 3, 3: 4}. Для чисел 4 и 2 в словаре пусто (значит, вернем для них -1).
    """

    # Словарь для хранения пар {num: greater_num}
    next_greater = {}
    # Монотонно убывающий стек
    stack: list[int] = []

    # Проходим по всем элементам nums2
    for num in nums2:
        # Пока стек не пуст и текущее число больше, чем число на вершине стека
        while stack and num > stack[-1]:
            popped_num = stack.pop()
            next_greater[popped_num] = num  # Фиксируем ответ для popped_num

        # Кладем текущее число в стек
        stack.append(num)

    # Формируем ответ для nums1, используя наш словарь
    return [next_greater.get(num, -1) for num in nums1]
