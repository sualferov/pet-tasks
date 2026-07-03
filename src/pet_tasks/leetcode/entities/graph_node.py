class GraphNode:
    """Definition for a GraphNode."""

    def __init__(
        self,
        val: int,
        neighbors: list[GraphNode] | None = None,
    ) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
