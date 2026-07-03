from collections import defaultdict, deque


def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """Определяет порядок прохождения курсов."""
    """
    В чем ключевые изменения?
    Инициализация: Вместо переменной processed_courses = 0 мы создали массив order = [].
    Сбор результата: Строка order.append(current) фиксирует курс в правильном топологическом порядке сразу,
    как только мы его "проходим" (извлекаем из очереди).
    Финальная проверка: Условие len(order) == numCourses проверяет, не застряли ли мы в цикле.
    Если в графе есть циклы, то некоторые узлы никогда не получат in_degree == 0 и не попадут в массив order.
    """

    # Шаг 1: Инициализируем граф и массив входящих степеней
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    # Шаг 2: Строим граф зависимостей
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Шаг 3: Очередь для курсов, у которых нет пререквизитов
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])

    # Список для хранения итогового порядка курсов
    order = []

    # Шаг 4: BFS обход (Топологическая сортировка)
    while queue:
        current = queue.popleft()
        order.append(current)  # Добавляем курс в итоговый путь

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Шаг 5: Проверяем, удалось ли включить все курсы (нет ли цикла)
    return order if len(order) == num_courses else []
