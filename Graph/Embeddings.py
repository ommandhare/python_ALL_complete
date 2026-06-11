import networkx as nx
from node2vec import Node2Vec

G = nx.Graph()

edges = [
    ("A", "B"),
    ("A", "D"),
    ("B", "C"),
    ("B", "E"),
    ("D", "E")
]

G.add_edges_from(edges)


node2vec = Node2Vec(
    G,
    dimensions=8,
    walk_length=10,
    num_walks=100,
    workers=2
)


model = node2vec.fit(
    window=5,
    min_count=1
)


embedding_A = model.wv["A"]

print(embedding_A)