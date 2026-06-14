def top_k_frequent_elements(nums: list[int], k: int) -> list[int]:
    """Возвращает список часто встречаемых элементов из списка."""
    """https://leetcode.com/problems/top-k-frequent-elements/"""
    if not nums:
        return []

    nums_counts: dict[int, int] = {}
    for num in nums:
        nums_counts.setdefault(num, 0)
        nums_counts[num] += 1

    counts_with_nums: list[list[int]] = [[] for _ in range(len(nums))]
    for num, count in nums_counts.items():
        counts_with_nums[count - 1].append(num)

    res_nums: list[int] = []
    for _nums in counts_with_nums[::-1]:
        if not _nums:
            continue
        if len(res_nums) >= k:
            break

        res_nums.extend(_nums)

    return res_nums
