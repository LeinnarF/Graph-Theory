from collections import deque

# DFS
def DFS(graph, start):
    visited = set()
    stack =[start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))
    

# BSF
def BFS(graph,start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Usage
graph = {
    'a': ['s', 'd'],
    'b': ['s', 'd'],
    'c': ['s', 'd'],
    'd': ['a', 'b', 'c'],
    's': ['a', 'b', 'c']
}
look = 's'

print("--DFS ",DFS(graph, look))
print("--BFS ",BFS(graph, look))