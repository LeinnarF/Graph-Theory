import networkx as nx
import matplotlib.pyplot as plt

# Define the edges
edges = [(4, 2), (2, 1), (6, 1), (1, 3), (3, 5), (7, 5), (5, 8)]

# Create a graph
G = nx.Graph()
G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(6, 6))
nx.draw(G, with_labels=True, font_size=14)
plt.show()
