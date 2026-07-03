class ListNode:
    """Элемент связанного списка."""

    def __init__(self, val: int = 0, next_node: ListNode | None = None):
        self.val = val
        self.next = next_node

    def add(self, val: int, nums: list[int] | None) -> None:
        """Добавляет следующий связанный элемент."""
        self.val = val

        if not nums:
            return

        self.next = ListNode()

        self.next.add(nums[0], nums[1:] if len(nums) > 1 else None)

    @classmethod
    def create(cls, nums: list[int]) -> ListNode | None:
        """Создает объект связанного списка."""
        if not nums:
            return None

        if len(nums) == 1:
            return ListNode(nums[0])

        head = ListNode()
        head.add(nums[0], nums=nums[1:])

        return head

    def __str__(self) -> str:
        curr: ListNode | None = self
        nums: list[str] = []
        while curr:
            nums.append(str(curr.val))
            curr = curr.next
        return ', '.join(nums)

    def to_list(self) -> list[int]:
        """Возвращает список int."""
        curr: ListNode | None = self
        nums: list[int] = []
        while curr:
            nums.append(curr.val)
            curr = curr.next
        return nums
