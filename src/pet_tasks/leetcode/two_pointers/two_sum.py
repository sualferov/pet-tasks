def two_sum(numbers: list[int], target: int) -> list[int]:
    """Возвращает индексы элементов массива, сумма элементов которых равна target."""
    """https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/"""
    if not numbers:
        return []

    idx_left, idx_right = 0, len(numbers) - 1

    while idx_left < idx_right:
        cur_sum = numbers[idx_left] + numbers[idx_right]
        if cur_sum == target:
            return [idx_left + 1, idx_right + 1]
        if cur_sum < target:
            idx_left += 1
            continue
        idx_right -= 1
    return []
