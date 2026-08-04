import networkx as nx
from node2vec import Node2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np


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
    sg=1,
    workers=1,
    seed=42,
    epochs=5
)


print("Embedding of Node")
print(model.wv["Om"])

print("Similar To OM....")
print(model.wv.most_similar("Om"))


# Get embeddings for every node
nodes = list(G.nodes())
embeddings = np.array([model.wv[node] for node in nodes])

from sklearn.manifold import TSNE

tsne = TSNE(
    n_components=2,
    perplexity=3,
    random_state=42,
    init="random"
)

embeddings_2d = tsne.fit_transform(embeddings)

# Plot
plt.figure(figsize=(8,6))

plt.scatter(
    embeddings_2d[:,0],
    embeddings_2d[:,1],
    s=400,
    color="skyblue",
    edgecolors="black"
)

# Add labels
for i, node in enumerate(nodes):
    plt.text(
        embeddings_2d[i,0] + 0.02,
        embeddings_2d[i,1] + 0.02,
        node,
        fontsize=11,
        fontweight="bold"
    )

plt.title("Node2Vec Embedding Visualization (PCA)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(alpha=0.3)

plt.show()


