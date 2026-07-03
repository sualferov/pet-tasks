# Мы связываем две структуры вместе.
#
# Двусвязный список (Doubly Linked List): хранит элементы в порядке их использования. У головы (head) будет лежать
# самый свежий элемент, у хвоста (tail) — самый устаревший (кандидат на удаление). Двусвязный список позволяет
# удалять и вставлять узлы за O(1), если у нас есть прямая ссылка на узел.
#
# Хэш-мапа (dict): хранит пары {ключ: ссылка_на_узел_в_списке}. Она обеспечивает мгновенный поиск узла за O(1).


class Node:
    """Класс связанного списка."""

    def __init__(self, key: int = 0, val: int = 0) -> None:
        self.key = key
        self.val = val
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:
    """Класс кеша."""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: dict[int, Node] = {}

        # Используем фейковые (dummy) узлы для головы и хвоста,
        # чтобы избежать постоянных проверок на None при удалении/вставке
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # Вспомогательный метод: удалить узел из любой точки списка
    @classmethod
    def _remove(cls, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node

    # Вспомогательный метод: вставить узел в самое начало (сразу после head)
    def _add_to_front(self, node: Node) -> None:
        next_node = self.head.next
        if not next_node:
            return

        self.head.next = node
        node.prev = self.head

        node.next = next_node
        next_node.prev = node

    # Вспомогательный метод: обновить статус использования узла (сделать самым свежим)
    def _make_recently_used(self, node: Node) -> None:
        self._remove(node)
        self._add_to_front(node)

    def get(self, key: int) -> int:
        """Возваращет элемент."""
        if key in self.cache:
            node: Node = self.cache[key]
            self._make_recently_used(node)  # Обновляем порядок использования
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        """Устанавливанет элемент."""
        if key in self.cache:
            # Если ключ уже есть, обновляем значение и двигаем вперед
            node = self.cache[key]
            node.val = value
            self._make_recently_used(node)
        else:
            # Если ключа нет, создаем новый узел
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

            # Если превысили лимит емкости, удаляем самый старый узел из хвоста
            if len(self.cache) > self.capacity:
                # Самый старый рабочий узел лежит прямо перед фейковым tail
                lru_node = self.tail.prev
                if lru_node:
                    self._remove(lru_node)
                    del self.cache[lru_node.key]  # Удаляем из хэш-мапы по ключу
