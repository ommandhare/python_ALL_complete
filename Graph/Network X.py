import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edges_from([
    ("Om", "jay"),
    ("Om", "Amit"),
    ("jay", "Priya"),
    ("Priya", "Amit"),
    ("Om","Prem")
])

print(f"Nodes --   {G.nodes()}")
print(f"Edges --  {G.edges()}")


print("Degree of Each Nodes")
for node in G.nodes():
    print(node, G.degree(node))


print("Neighbours of Particular Nodes")
print(list(G.neighbors("Om")))

print("Shortest Path for NODE A to NODE B")

path = nx.shortest_path(
    G,
    source="Prem",
    target="Priya"
)

print(path)




nx.draw(G, with_labels=True)

plt.show()


