import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, u, v, weight):
        self.graph.add_edge(u, v, weight=weight)

    def dijkstra(self, start):
        shortest_paths = {node: float('inf') for node in self.graph.nodes}
        shortest_paths[start] = 0
        
        priority_queue = [(0, start)]  
        predecessors = {}  

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            for neighbor in self.graph.neighbors(current_node):
                weight = self.graph[current_node][neighbor]['weight']
                distance = current_distance + weight

                if distance < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        return shortest_paths, predecessors

    def get_shortest_path(self, predecessors, start, target):
        
        path = []
        current = target
        while current != start:
            path.append(current)
            current = predecessors.get(current, None)
            if current is None:
                return None  
        path.append(start)
        return path[::-1]  

    def draw_graph(self, title="Graph"):
        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        
        plt.figure(figsize=(8, 6))
        nx.draw(self.graph, pos, with_labels=True, node_color="lightblue", node_size=500, edge_color="black", font_size=12)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        
        plt.title(title)
        plt.show()


G = Graph()

# Add travel times as weighted edges
travel_time = [
    ('A', 'B', 12),
    ('A', 'C', 20),
    ('A', 'E', 35),
    ('B', 'C', 8),
    ('B', 'D', 25),
    ('B', 'F', 10),
    ('C', 'D', 10),
    ('C', 'E', 18),
    ('D', 'E', 15),
    ('D', 'F', 5),
    ('E', 'F', 7)
]

for u, v, w in travel_time:
    G.add_edge(u, v, w)

# Draw the travel time graph
G.draw_graph("Travel Time Graph")

# Set starting point and destination
source = 'A'
destination = 'D'

# Run Dijkstra’s algorithm
shortest_paths, predecessors = G.dijkstra(source)

# Get shortest path from source to destination
shortest_path = G.get_shortest_path(predecessors, source, destination)

# Display shortest paths from source
print(f"Shortest travel times from {source}:")
for node, distance in shortest_paths.items():
    print(f"  - To {node}: {distance} minutes")

# Display the traversed nodes (shortest path)
if shortest_path:
    print(f"\nFastest route from {source} to {destination}: {' -> '.join(shortest_path)}")
    print(f"Total travel time: {shortest_paths[destination]} minutes")
else:
    print(f"No path found from {source} to {destination}.")
