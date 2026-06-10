class ContiguousArray:
    """Находит в списке кол-во элементов с наибольшим списком элементов [x, j]."""

    """
    https://leetcode.com/problems/contiguous-array/
    [0,1,0] -> [0,1] | [1,0] = 2
    [0,1,1,1,1,1,0,0,0] -> [1,1,1,0,0,0] = 6
    """

    @classmethod
    def find_max_length(cls, nums: list[int]) -> int:
        """Определяет максимальную длину под-массива с одинаковым кол-вом 1,0."""
        max_length = 0
        min_nums_length = 2

        if len(nums) < min_nums_length:
            return max_length

        prev_sub_array = ''
        prev_element = nums[0]
        sub_array = str(nums[0])
        for idx, num in enumerate(nums):
            if idx == 0:
                continue

            if num != prev_element:
                max_length = min(len(prev_sub_array), len(sub_array))
                prev_sub_array = sub_array
                sub_array = str(num)
            else:
                sub_array += str(num)

            prev_element = num

        if sub_array:
            max_length = min(len(prev_sub_array), len(sub_array))

        return max_length * 2
