from collections import deque

def dfs_recursive(graph, vertex, goal, visited=None, path=None):
    if visited is None:
        visited = set()  
    if path is None:
        path = []  
    visited.add(vertex)
    path.append(vertex) 
    if vertex == goal:  
        return path
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            result = dfs_recursive(graph, neighbor, goal, visited, path)
            if result:  
                return result
    path.pop() 
    return None

def dfs_iterative(graph, start_vertex, goal_vertex):
    visited = set()  
    stack = [(start_vertex, [start_vertex])] 
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            visited.add(vertex)  
            if vertex == goal_vertex:
                return path
            for neighbor in reversed(list(graph[vertex])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None 

def bfs_recursive(graph, queue, goal_vertex, visited=None):
    # Перевіряємо, чи передана черга є рядком, і перетворюємо її на deque
    if isinstance(queue, str):
        queue = deque([(queue, [queue])])

    # Ініціалізуємо відвідані вершини, якщо вони не були передані
    if visited is None:
        visited = set()

    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return None

    # Вилучаємо вершину з початку черги разом з її шляхом
    vertex, path = queue.popleft()

    # Перевіряємо, чи була вершина відвідана раніше
    if vertex not in visited:
        visited.add(vertex)  # Відмічаємо вершину як відвідану

        # Якщо знайшли цільову вершину, повертаємо шлях до неї
        if vertex == goal_vertex:
            return path

        # Додаємо невідвіданих сусідів даної вершини в кінець черги з оновленим шляхом
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    # Рекурсивний виклик функції з оновленою чергою і відвіданими вершинами
    return bfs_recursive(graph, queue, goal_vertex, visited)





def bfs_iterative(graph, start_vertex, goal_vertex):
    visited = set()
    queue = deque([(start_vertex, [start_vertex])])
    while queue:  
        (vertex, path) = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            if vertex == goal_vertex:
                return path
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None