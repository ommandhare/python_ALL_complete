import networkx as nx
from node2vec import Node2Vec


G = nx.Graph()

G.add_edges_from([
    ("A","B"),
    ("B","C"),
    ("B","E"),
    ("C","D")
])


node2vec = Node2Vec(
    G,
    dimensions=16,
    walk_length=10,
    num_walks=100,
    p=1,
    q=0.5
)

model = node2vec.fit(
    window=5,
    min_count=1
)

print(model.wv["A"])