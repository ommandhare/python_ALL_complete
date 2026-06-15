import networkx as nx

G = nx.Graph()

G.add_edges_from([
    ("A","B"),
    ("A","C"),
    ("B","D"),
    ("C","D"),
    ("D","E"),
    ("E","F")
])

print("Centrality ... ")
degree = nx.degree_centrality(G)

for node, score in degree.items():
    print(node, round(score,3))

print("Betweness of Centrality...")
bet = nx.betweenness_centrality(G)

for node, score in bet.items():
    print(node, round(score,3))


print("Closeness of Centrality...")

close = nx.closeness_centrality(G)

for node, score in close.items():
    print(node, round(score,3))

print("Connected Components...")
G = nx.Graph()

G.add_edges_from([
    ("A","B"),
    ("B","C"),
    ("D","E")
])

components = list(nx.connected_components(G))

print(components)

