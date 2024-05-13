import networkx as nx
import matplotlib.pyplot as plt

#Task_1

G = nx.Graph()

stops = ["Центр", "Сихів", "Личаківський район", "Франківський район", "Залізничний район", "Винники"]

routes = [
    ("Центр", "Сихів"),
    ("Центр", "Франківський район"),
    ("Личаківський район", "Франківський район"),
    ("Залізничний район", "Сихів"),
    ("Винники", "Центр")
]

G.add_nodes_from(stops)
G.add_edges_from(routes)


nx.draw(G, with_labels=True)
plt.title("Граф уявної транспортної мережі м. Львова")
plt.show()

number_of_nodes = G.number_of_nodes()
number_of_edges = G.number_of_edges()
degrees = G.degree()

print(f"Кількість вершин: {number_of_nodes}")
print(f"Кількість ребер: {number_of_edges}")
print(f"Ступені вершин: {degrees}")

#Task_2

def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    dfs_order = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            dfs_order.append(vertex)
            visited.add(vertex)
            stack.extend(reversed([v for v in graph[vertex] if v not in visited]))

    return dfs_order

def bfs_iterative(graph, start):
    visited = set()
    queue = [start]
    bfs_order = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            bfs_order.append(vertex)
            visited.add(vertex)
            queue.extend([v for v in graph[vertex] if v not in visited])

    return bfs_order

start_vertex = "Центр"
dfs_result = dfs_iterative(G, start_vertex)
bfs_result = bfs_iterative(G, start_vertex)

dfs_result, bfs_result

#Task_3

edge_weights= [
    ("Центр", "Сихів", {"weight": 7}),
    ("Центр", "Франківський район", {"weight": 3}),
    ("Личаківський район", "Франківський район", {"weight": 5}),
    ("Залізничний район", "Сихів", {"weight": 6}),
    ("Винники", "Центр", {"weight": 8})
]
G.add_edges_from(edge_weights)

import heapq

def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

dijkstra_result = dijkstra(G, "Центр")
dijkstra_result