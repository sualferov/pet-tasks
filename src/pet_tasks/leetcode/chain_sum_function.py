class ChainSum(int):
    """Суммирование цепочек вызовов."""

    def __init__(self, number: int | None = 0):
        self._number = number or 0

    def __call__(self, number: int | None = 0) -> ChainSum:
        """Описание."""
        number = number or 0
        return ChainSum(self._number + number)

    def __str__(self) -> str:
        return str(self._number)


chain_sum = ChainSum
