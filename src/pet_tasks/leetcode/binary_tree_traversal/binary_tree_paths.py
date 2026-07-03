from pet_tasks.leetcode.entities.tree_node import TreeNode


def binary_tree_paths(root: TreeNode | None = None) -> list[str]:
    """Возвращает пути обхода дерева."""
    """
    Сложность по времени O(N), по памяти O(H - глубина дерева)
    """
    if not root:
        return []

    ans = []
    # Инициализируем стек парой (узел, строка_пути)
    stack = [(root, str(root.val))]

    while stack:
        node, path = stack.pop()

        # Если это лист — фиксируем путь в ответе
        if not node.left and not node.right:
            ans.append(path)

        # Кладем в стек правого потомка (он обработается позже левого)
        if node.right:
            stack.append((node.right, f'{path}->{node.right.val}'))
        # Кладем в стек левого потомка (он обработается раньше, так как попадет на вершину)
        if node.left:
            stack.append((node.left, f'{path}->{node.left.val}'))

    return ans


def binary_tree_paths_recursion(root: TreeNode | None = None) -> list[str]:
    """Рекурсивный бинарный поиск."""
    result = []

    def dfs(node: TreeNode | None, current_path: str) -> None:
        if not node:
            return

        # Конструируем путь для текущего узла
        if current_path:
            current_path += f'->{node.val}'
        else:
            current_path = str(node.val)

        # Если это лист, сохраняем результат
        if not node.left and not node.right:
            result.append(current_path)
            return

        # Рекурсивный спуск в поддеревья
        if node.left:
            dfs(node.left, current_path)
        if node.right:
            dfs(node.right, current_path)

    dfs(root, '')
    return result
