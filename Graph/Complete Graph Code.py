import networkx as nx
from node2vec import Node2Vec
import matplotlib.pyplot as plt

G = nx.Graph()


G.add_edges_from([
    ("Om", "Python"),
    ("Om", "SQL"),
    ("Python", "Pandas"),
    ("Python", "Rahul"),
    ("SQL", "Database"),
    ("Rahul", "MachineLearning"),
    ("Pandas", "MachineLearning")
])
nx.draw(
    G,
    with_labels=True,
    node_size=2000
)

plt.show()

node2vec = Node2Vec(
    G,
    dimensions=16,
    walk_length=5,
    num_walks=10,
    p=1,
    q=1,
    workers=1,
    seed=42
)

model = node2vec.fit(
    window=5,
    min_count=1,
    batch_words=4
)
print("Embedding of Node")
print(model.wv["Om"])

print("Similar To OM....")
print(model.wv.most_similar("Om"))




