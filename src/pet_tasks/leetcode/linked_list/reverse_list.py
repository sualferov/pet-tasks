# Сложность: O(N) & O(1)
# Сложность для рекурсии: O(N) & O(N)


from pet_tasks.leetcode.linked_list.list_node import ListNode


def reverse_list(head: ListNode | None = None) -> ListNode | None:
    """Разворачивает переданный список."""
    if not head:
        return None

    prev: ListNode | None
    curr: ListNode | None
    prev, curr = None, head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    return prev


def reverse_list_recursive(head: ListNode | None) -> ListNode | None:
    """Разворачивает переданный список рекурсивно."""
    # Базовый случай: если список пуст или дошли до последнего узла
    if not head or not head.next:
        return head

    # Рекурсивно разворачиваем весь список, начиная со следующего узла
    new_head = reverse_list_recursive(head.next)

    # Разворачиваем связь между текущим узлом и следующим
    # Было: head -> head.next
    # Делаем: head.next.next -> head (следующий узел теперь указывает на текущий)
    head.next.next = head
    head.next = None  # Обнуляем старую связь, чтобы избежать зацикливания

    return new_head
