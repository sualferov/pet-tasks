from pet_tasks.leetcode.entities.tree_node import TreeNode


def path_sum(root: TreeNode, target_sum: int) -> list[list[int]]:
    """Возвращает путь."""
    """
    Концепция DFS + Backtracking

    Вместо того чтобы копировать массив путей на каждом шаге рекурсии (что неэффективно по памяти),
    мы будем использовать один общий список current_path.

    1. Шаг вперед: Заходя в узел, мы добавляем его значение в current_path и вычитаем его из targetSum.
    2. Проверка листа: Если мы дошли до листа и targetSum == 0, мы нашли нужный путь. Мы делаем его глубокую копию
        (list(current_path)) и добавляем в итоговый ответ.
    3. Шаг назад (Backtrack): Перед выходом из функции (возвратом к родителю) мы удаляем текущий узел из общего
        списка (current_path.pop()). Это гарантирует, что при исследовании других веток дерева состояние
        пути останется чистым.
    """
    ans = []
    current_path = []

    def dfs(node: TreeNode | None, current_target: int) -> None:
        if not node:
            return

        # Шаг 1: Добавляем текущий узел в путь
        current_path.append(node.val)

        # Базовый случай: мы пришли в лист
        if not node.left and not node.right:
            # Если сумма совпала, сохраняем КОПИЮ текущего пути
            if current_target == node.val:
                ans.append(list(current_path))
        else:
            # Рекурсивный спуск в поддеревья с уменьшенным таргетом
            dfs(node.left, current_target - node.val)
            dfs(node.right, current_target - node.val)

        # Шаг 2: Backtracking — удаляем себя из пути перед возвратом наверх
        current_path.pop()

    dfs(root, target_sum)
    return ans
