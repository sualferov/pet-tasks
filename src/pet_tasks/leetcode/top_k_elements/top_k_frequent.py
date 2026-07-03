import heapq
from collections import Counter


def top_k_frequent_heap(nums: list[int], k: int) -> list[int]:
    """Возвращает список часто встречаемых элементов из списка."""
    """
    Время: O(Nlog N), Память: O(1) или O(N).
    """
    # Шаг 1: Считаем частоту каждого числа — O(N) по времени и памяти
    count = Counter(nums)

    # Шаг 2: Храним в мин-куче ровно k элементов. Сравниваем по частоте.
    # В Python heapq сравнивает кортежи по первому элементу: (частота, число)
    min_heap: list[tuple[int, int]] = []

    for num, freq in count.items():
        heapq.heappush(min_heap, (freq, num))
        # Если куча превысила размер k, выталкиваем элемент с наименьшей частотой
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Шаг 3: Достаем числа из кучи
    return [num for freq, num in min_heap]


def top_k_frequent_elements(nums: list[int], k: int) -> list[int]:
    """Возвращает список часто встречаемых элементов из списка."""
    """
    Время: O(N), Память: O(N).
    """
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
