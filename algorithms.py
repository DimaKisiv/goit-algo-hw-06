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
    if isinstance(queue, str):
        queue = deque([(queue, [queue])])
    if visited is None:
        visited = set()
    if not queue:
        return None
    vertex, path = queue.popleft()
    if vertex not in visited:
        visited.add(vertex)  
        if vertex == goal_vertex:
            return path

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

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


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.nodes()}
    distances[start] = 0
    visited = set()
    while len(visited) < len(graph.nodes()):
        min_vertex = None
        for vertex in graph.nodes():
            if vertex not in visited:
                if min_vertex is None or distances[vertex] < distances[min_vertex]:
                    min_vertex = vertex
        if distances[min_vertex] == float('infinity'):
            break
        visited.add(min_vertex)
        for neighbor in graph.neighbors(min_vertex):
            weight = graph[min_vertex][neighbor]['weight']
            new_distance = distances[min_vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
    return distances