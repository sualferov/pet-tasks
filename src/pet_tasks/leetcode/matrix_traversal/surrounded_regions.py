"""Сложность алгоритма.

Time Complexity: O(MxN) — каждую клетку мы посещаем фиксированное количество раз.
Space Complexity: O(MxN) — в худшем случае (когда вся матрица состоит из 'O')

Если решать задачу «в лоб», проверяя каждую группу O на окруженность, код получится перегруженным.
Ключевое свойство: любая клетка O, которая соединена с границей матрицы, НЕ может быть окружена.
Поэтому мы применим стратегию «от обратного» (Border-First Search):
    Пройдемся по всем четырем границам матрицы.
    Если находим там O, запускаем обход (DFS или BFS) и временно перекрашиваем эту клетку и все связанные
    с ней внутренние O в какой-нибудь нейтральный символ (например, 'E' — Escaped/Спасенные).
    После этого делаем финальный проход по всей матрице:
        Все оставшиеся O гарантированно окружены X — превращаем их в X.
        Все 'E' — это спасенные клетки, возвращаем им исходный вид O.
"""
from collections import deque


def surrounded_regions_recursion(board: list[list[str]]) -> None:
    """Заменяет окруженные O на X."""
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int) -> None:
        # Проверяем границы и что клетка действительно является 'O'
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
            return

        # Маркируем как "спасенную" от окружения клетку
        board[r][c] = 'E'

        # Обходим 4 соседние стороны
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Шаг 1: Запускаем DFS из всех 'O' на левой и правой границах
    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)

    # Шаг 1 (продолжение): Запускаем DFS из всех 'O' на верхней и нижней границах
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)

    # Шаг 2: Финальный скан и восстановление матрицы
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'  # Были окружены -> заменяем на 'X'
            elif board[r][c] == 'E':
                board[r][c] = 'O'  # Были соединены с границей -> возвращаем 'O'


def surrounded_regions_no_recursion(board: list[list[str]]) -> None:
    """Заменяет окруженные O на X (без рекурсии)."""
    if not board or not board:
        return

    rows, cols = len(board), len(board)
    queue: deque[tuple[int, int]] = deque()

    # Шаг 1: Собираем в очередь все граничные клетки, если они равны 'O'
    # Левая и правая границы
    for r in range(rows):
        if board[r][0] == 'O':
            queue.append((r, 0))
        if board[r][cols - 1] == 'O':
            queue.append((r, cols - 1))

    # Верхняя и нижняя границы (пропускаем углы, они уже добавлены)
    for c in range(1, cols - 1):
        if board[0][c] == 'O':
            queue.append((0, c))
        if board[rows - 1][c] == 'O':
            queue.append((rows - 1, c))

    # Шаг 2: Итеративный BFS
    # Расходимся от границ внутрь матрицы
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        r, c = queue.popleft()

        # Проверяем, не обработали ли мы эту клетку ранее
        if board[r][c] == 'O':
            board[r][c] = 'E'  # Маркируем как "спасенную"

            # Добавляем всех соседей в очередь
            for dr, dc in directions:
                row, col = r + dr, c + dc
                # Если сосед в границах и он тоже 'O' — отправляем на обработку
                if 0 <= row < rows and 0 <= col < cols and board[row][col] == 'O':
                    queue.append((row, col))

    # Шаг 3: Финальный проход и трансформация матрицы
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'  # Окруженные клетки -> 'X'
            elif board[r][c] == 'E':
                board[r][c] = 'O'  # Спасенные клетки -> возвращаем 'O'
