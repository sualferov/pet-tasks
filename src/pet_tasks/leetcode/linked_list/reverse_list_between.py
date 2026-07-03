# Сложность: O(N) & O(1)
# Чтобы избежать лишних проверок (например, когда left = 1 и меняется голова списка),
# мы снова используем паттерн Dummy Node [url].
# Алгоритм делится на три понятных шага:
#     Доходим до точки старта: Сдвигаем указатель prev так, чтобы он остановился ровно перед началом разворота
#     (на позиции left - 1).
#
#     Локальный разворот (Паттерн перестановки): Узел сразу после prev назовем curr (это будет первый
#     элемент разворачиваемой части). Мы не будем классически разворачивать стрелки, мы будем «вытаскивать»
#     следующий за curr элемент и переставлять его сразу после prev. Повторяем это right - left раз.
#
#     Возврат результата: Возвращаем dummy.next
#
# Визуализация магии цикла (для пары left=2, right=4 на списке 1 -> 2 -> 3 -> 4 -> 5):
# Перед циклом: prev указывает на 1, curr указывает на 2.
# Итерация 1 (переносим 3): Список становится 1 -> 3 -> 2 -> 4 -> 5. (curr всё еще 2, но теперь указывает на 4).
# Итерация 2 (переносим 4): Список становится 1 -> 4 -> 3 -> 2 -> 5. Разворот завершен!

from pet_tasks.leetcode.linked_list.list_node import ListNode


def reverse_list_between(left: int, right: int, head: ListNode | None = None) -> ListNode | None:
    """Разворачивает переданный список в заданном интервале."""
    if not head:
        return None

    if left == right:
        return head

    # Создаем dummy узел, чтобы легко обрабатывать случай left = 1
    dummy = ListNode(val=0, next_node=head)

    # 1. Доходим до узла, который стоит прямо перед началом разворота
    pre: ListNode | None = dummy
    for _ in range(left - 1):
        pre = pre.next if pre else None

    # 2. Инициализируем указатель на первый элемент, который будем разворачивать
    curr = pre.next if pre else None

    # 3. Разворачиваем связи внутри диапазона (right - left) раз
    # Используем метод вставки элемента на позицию сразу после 'pre'
    for _ in range(right - left):
        if not curr:
            continue
        nxt = curr.next
        curr.next = nxt.next if nxt else None
        if nxt:
            nxt.next = pre.next if pre else None
        if pre:
            pre.next = nxt

    return dummy.next
