def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {}
num_vertices = int(input("Enter the number of vertices: "))

for i in range(num_vertices):
    vertex = input(f"Enter vertex {i + 1}: ")
    neighbors = input(f"Enter neighbors of vertex {vertex}: ").split()
    graph[vertex] = neighbors

start_vertex = input("Enter the start vertex for DFS: ")

print("DFS traversal:")
dfs(graph, start_vertex)
