import heapq
import random


def find_k_largest_heap(nums: list[int], k: int) -> int:
    """Находит k-ый наибольший элемент."""
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    # Итерируемся по оставшимся элементам
    for num in nums[k:]:
        # Если текущее число больше, чем самый маленький элемент в куче
        if num > min_heap[0]:
            # Выталкиваем старый минимум и вставляем новое число
            heapq.heappushpop(min_heap, num)

    # На вершине кучи лежит k-й по величине элемент
    return min_heap[0]


def find_k_largest_element(nums: list[int], k: int) -> int:
    """Находит k-ый наибольший элемент."""
    """
    Обычно на собеседовании интервьюер ждет от вас эволюции мысли от простого решения к оптимальному:
    Наивное решение (Сортировка):
        Отсортировать массив по убыванию и вернуть элемент на индексе k-1.
        Время: O(Nlog N), Память: O(1) или O(N).
    Оптимальное решение (Мин-куча / Min-Heap):
        Поддерживать кучу размером ровно k элементов.
        Время: O(Nlog k), Память: O(k).
    Решение для обсуждения (QuickSelect):
        Алгоритм поиска, похожий на QuickSort.
        В среднем работает за O(N), но в худшем случае деградирует до O(N^2)
    """
    # Нам нужен K-й наибольший элемент.
    # В терминах отсортированного по возрастанию массива это индекс: len(nums) - k
    if not nums:
        return 0

    target_idx = len(nums) - k

    def quickselect(left: int, right: int) -> int:
        # Выбираем случайный pivot и меняем его с крайним правым элементом
        pivot_idx = random.randint(left, right)
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

        pivot = nums[right]
        fill_idx = left

        # Разделение массива (Partition)
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[i], nums[fill_idx] = nums[fill_idx], nums[i]
                fill_idx += 1

        # Помещаем pivot на его итоговое правильное место
        nums[fill_idx], nums[right] = nums[right], nums[fill_idx]

        # Проверяем, угадали ли мы индекс
        if fill_idx == target_idx:
            return nums[fill_idx]
        if fill_idx < target_idx:
            return quickselect(fill_idx + 1, right)
        return quickselect(left, fill_idx - 1)

    return quickselect(0, len(nums) - 1)
