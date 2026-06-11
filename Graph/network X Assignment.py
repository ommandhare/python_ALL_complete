import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edges_from([
    ("Om", "SQL"),
    ("SQL", "Python"),
    ("Om","Python"),
    ("Om", "Pandas"),
    ("Pandas", "Rahul")
])

print(f"Nodes --   {G.nodes()}")
print(f"Edges --  {G.edges()}")

print("Degree of Each Nodes")
for node in G.nodes():
    print(node, G.degree(node))

print("Neighbours of Particular Nodes")
print(list(G.neighbors("Om")))

nx.draw(G, with_labels=True)

plt.show()