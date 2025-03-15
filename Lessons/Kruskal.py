import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.Graph()
    
    def add_vertices(self, vertices):
        self.graph.add_nodes_from(vertices)
    
    def add_edge(self, u, v, weight):
        self.graph.add_edge(u, v, weight=weight)
    
    def vertices(self):
        return list(self.graph.nodes)
    
    def edges(self):
        return list(self.graph.edges(data=True))  # (u, v, {'weight': w})

def kruskal_mst(graph):
    mst = Graph()
    mst.add_vertices(graph.vertices())

    edges = sorted(graph.edges(), key=lambda x: x[2]['weight'])  # Sort edges by weight
    parent = {v: v for v in graph.vertices()}

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            parent[root2] = root1

    for u, v, attr in edges:
        if find(u) != find(v):
            mst.add_edge(u, v, attr['weight'])
            union(u, v)

    return mst

def draw_graph(graph, title="Graph"):
    pos = nx.spring_layout(graph.graph)  # Layout for visualization
    labels = nx.get_edge_attributes(graph.graph, 'weight')
    
    plt.figure(figsize=(8, 6))
    nx.draw(graph.graph, pos, with_labels=True, node_color="lightblue", node_size=500, edge_color="black", font_size=12)
    nx.draw_networkx_edge_labels(graph.graph, pos, edge_labels=labels)
    
    plt.title(title)
    plt.show()

# Define the graph
G = Graph()

# Add barangays as vertices
barangays = ['Atlag', 'Bagna', 'Balayong', 'San Juan', 'Sto Cristo', 'Sto Rosario']
G.add_vertices(barangays)

# Add edges with weights
barangay_pairs = [
    ('Atlag', 'Bagna', 5),
    ('Atlag', 'Balayong', 7),
    ('Atlag', 'San Juan', 10),
    ('Bagna', 'Balayong', 8),
    ('Bagna', 'Sto Cristo', 12),
    ('Bagna', 'Sto Rosario', 6),
    ('Balayong', 'Sto Cristo', 4),
    ('Balayong', 'San Juan', 9),
    ('Sto Cristo', 'San Juan', 11),
    ('Sto Cristo', 'Sto Rosario', 3),
    ('San Juan', 'Sto Rosario', 2)
]

for u, v, w in barangay_pairs:
    G.add_edge(u, v, w)

# Draw the original graph
draw_graph(G, "Barangay Connection Graph")

# Generate and draw the Minimum Spanning Tree (MST)
mst = kruskal_mst(G)
draw_graph(mst, "Minimum Spanning Tree (MST) using Kruskal's Algorithm")

# Generate and draw the Minimum Spanning Tree (MST)
mst = kruskal_mst(G)

# Print the pairs of barangays for the new MST
print("Pairs of barangays in the MST:")
total_cost = 0
for u, v, attr in mst.edges():
    print(f"{u} - {v} (weight: {attr['weight']})")
    total_cost += attr['weight']

# Print the minimum total cost
print(f"Minimum total cost: {total_cost}")

draw_graph(mst, "Minimum Spanning Tree (MST) using Kruskal's Algorithm")
