class RangeSum:
    """Рассчитывает сумму элементов массива в интервале [i,j]."""

    """https://leetcode.com/problems/range-sum-query-immutable/"""

    def __init__(self, nums: list[int]):
        self.nums_sum = []
        for idx, num in enumerate(nums):
            if idx == 0:
                self.nums_sum.append(num)
            else:
                self.nums_sum.append(self.nums_sum[idx - 1] + num)

    def sum_range(self, left: int, right: int) -> int:
        """Возвращает сумму элекментов в интервале [left, right]."""
        return self.nums_sum[right] if left == 0 else self.nums_sum[right] - self.nums_sum[left - 1]
