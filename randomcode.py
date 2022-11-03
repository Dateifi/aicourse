graph = {
    'aranos': {'barlow': 14, 'daxx': 7, 'yeedil': 9},
    'boldan': {'barlow': 9, 'oozla': 6},
    'barlow': {'aranos': 14, 'boldan': 9, 'yeedil': 2},
    'daxx': {'aranos': 7, 'yeedil': 10, 'oozla': 16},
    'yeedil': {'aranos': 9, 'barlow': 2, 'daxx': 10, 'oozla': 11},
    'oozla': {'boldan': 6, 'daxx': 15, 'yeedil': 11},
}


def dijkstra_shortest_path(source, destination):
    visited = set()
    distances = {source: 0}
    previous = {}
    while len(visited) < len(graph):
        current = min(distances, key=lambda x: distances[x] if x not in visited else float('inf'))
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                new_distance = distances[current] + graph[current][neighbor]
                if neighbor not in distances or new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current
    path = []
    current = destination
    while current != source:
        path.append(current)
        current = previous[current]
    path.append(source)
    path.reverse()
    return path


routes = [dijkstra_shortest_path('aranos', 'boldan'), dijkstra_shortest_path('barlow', 'aranos'),
          dijkstra_shortest_path('daxx', 'boldan')]

for route in routes:
    cost = 0
    for i in range(1, len(route)):
        print(f"{route[i-1].capitalize()} -> {graph[route[i-1]][route[i]]} -> {route[i].capitalize()}")
        cost += graph[route[i-1]][route[i]]
    print(f"Total fuel cost: {cost}\n")

