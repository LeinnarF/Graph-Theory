import heapq
import networkx as nx
import matplotlib.pyplot as plt

def prim_mst(edges):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    
    start_node = list(G.nodes)[0]  # Start from any node
    mst = []
    total_cost = 0
    
    visited = set([start_node])
    edges_heap = [(weight, start_node, v) for u, v, weight in G.edges(start_node, data='weight')]
    heapq.heapify(edges_heap)
    
    while edges_heap:
        weight, u, v = heapq.heappop(edges_heap)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_cost += weight
            
            for _, neighbor, w in G.edges(v, data='weight'):
                if neighbor not in visited:
                    heapq.heappush(edges_heap, (w, v, neighbor))
    
    return mst, total_cost

# Given edges
edges = [
    ('A', 'C', 10),
    ('A', 'B', 11),
    ('B', 'C', 12),
    ('B', 'D', 16),
    ('B', 'F', 19),
    ('C', 'E', 5),
    ('C', 'G', 7),
    ('D', 'F', 20),
    ('D', 'H', 13),
    ('E', 'G', 9),
    ('E', 'J', 15),
    ('F', 'G', 14),
    ('G', 'I', 17),
    ('H', 'I', 6),
    ('I', 'J', 18),
    ('I', 'F', 8)
]

# Compute MST
mst, total_cost = prim_mst(edges)

# Print the result
print("Minimum Spanning Tree Edges:")
for edge in mst:
    print(edge)
print(f"Total Cost of MST: {total_cost}")

# Draw the MST
graph = nx.Graph()
graph.add_weighted_edges_from(mst)
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
plt.show()
