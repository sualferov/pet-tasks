def two_sum(nums: list[int], target: int) -> list[int]:
    """Проверяет наличие заданной суммы соседних элементов."""
    terms: dict[int, int] = {}

    for i, num in enumerate(nums):
        remainder = target - num
        if remainder in terms:
            return [terms[remainder], i]
        terms[num] = i
    return []
