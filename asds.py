graph = {
    'aranos': {'barlow': 14, 'daxx': 7, 'yeedil': 9},
    'boldan': {'barlow': 9, 'oozla': 6},
    'barlow': {'aranos': 14, 'boldan': 9, 'yeedil': 2},
    'daxx': {'aranos': 7, 'yeedil': 10, 'oozla': 16},
    'yeedil': {'aranos': 9, 'barlow': 2, 'daxx': 10, 'oozla': 11},
    'oozla': {'boldan': 6, 'daxx': 16, 'yeedil': 11},
}

import sys
import heapq
def dijkstra_pathfinder(graph, source, destination):
    # Maximum value for initialization
    inf = sys.maxsize
    
    # Create dict of nodes with cost and previous nodes, and set source cost to 0
    planet_table = {}
    for node in graph:
        planet_table[node] = {'cost':inf, 'prev':[]}
    planet_table[source]['cost'] = 0
        
    # Initialize source node as first visited, and empty list of visited nodes

    visited = {}
    min_heap = [(0, source)]
    
    # Pathfinding
    for i in range(len(graph)-1):
        for item in min_heap:
            if item[1] not in visited or item[0] < visited[item[1]]:
                visited[item[1]] = item[0]

            for j in graph[item[1]]:
                if j not in visited:
                    cost = planet_table[item[1]]['cost'] + graph[item[1]][j]
                    if cost < planet_table[j]['cost']:
                        planet_table[j]['cost'] = cost
                        s = []
                        s.append(''.join(list(item[1])))
                        planet_table[j]['prev'] = planet_table[item[1]]['prev'] + s
                    heapq.heappush(min_heap, (planet_table[j]['cost'], j))
        heapq.heapify(min_heap)

        print(min_heap)
        print(visited)
        print(item[1])
        
    
    # Adding destination to list of nodes visited
    planet_table[destination]['prev'].append(destination)
    
    # Function to generate path string, only to be used inside this function
    def path_helper(lst):
        path = ''
        for i in lst:
            if i != lst[-1]:
                path += i + " -> "
            else:
                path += i + "."
        return path
    
    return f"Cost to travel from {source} to {destination} is {planet_table[destination]['cost']}, and the path taken is: {path_helper(planet_table[destination]['prev'])}"
    
        
print(dijkstra_pathfinder(graph, 'oozla', 'barlow'))