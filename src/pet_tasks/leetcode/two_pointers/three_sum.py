def three_sum(numbers: list[int]) -> list[list[int]]:
    """Возвращает массивы из 3 элементов, сумма которых равна 0."""
    """https://leetcode.com/problems/3sum/description/"""
    numbers.sort()
    result: list[list[int]] = []
    length = len(numbers)

    for i in range(length - 2):
        # Пропускаем одинаковые элементы для первого числа, чтобы избежать дубликатов
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue

        # Оптимизация: если текущее число > 0, сумма трех чисел точно будет > 0
        if numbers[i] > 0:
            break

        left, right = i + 1, length - 1

        while left < right:
            current_sum = numbers[i] + numbers[left] + numbers[right]

            if current_sum == 0:
                result.append([numbers[i], numbers[left], numbers[right]])
                left += 1
                right -= 1

                # Пропускаем дубликаты для второго числа
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                # Пропускаем дубликаты для третьего числа
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1

            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result
