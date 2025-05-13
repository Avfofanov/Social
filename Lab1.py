import heapq
def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor in range(n):
            weight = graph[current_vertex][neighbor]
            if weight > 0:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
    return distances
graph = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0],
]
start_vertex = 0
distances = dijkstra(graph, start_vertex)
print(f"Кратчайшие расстояния от вершины {start_vertex}:")
for i, dist in enumerate(distances):
    print(f"До вершины {i}: {dist}")
