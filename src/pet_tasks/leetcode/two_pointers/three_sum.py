def three_sum(numbers: list[int]) -> list[list[int]]:
    """Возвращает массивы из 3 элементов, сумма которых равна 0."""
    """https://leetcode.com/problems/3sum/description/"""
    min_numbers_length = 3
    if not numbers or len(numbers) < min_numbers_length:
        return []

    numbers.sort()
    idx_left, idx_middle, idx_right = 0, 1, len(numbers) - 1

    sum_elements: list[list[int]] = []

    while idx_left <= len(numbers) - 2:
        num_left = numbers[idx_left]

        while idx_middle < idx_right:
            num_middle, num_right = numbers[idx_middle], numbers[idx_right]

            if (
                num_middle + num_right + num_left == 0
                and [num_left, num_middle, num_right] not in sum_elements
            ):
                sum_elements.append([num_left, num_middle, num_right])
            if num_middle + num_right + num_left < 0:
                idx_middle += 1
                continue
            idx_right -= 1

        idx_left += 1
        idx_middle = idx_left + 1
        idx_right = len(numbers) - 1

    return sum_elements
