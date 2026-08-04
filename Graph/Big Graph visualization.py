# ==========================================================
# Graph Embedding Visualization using Node2Vec
# Network Graph -> Node2Vec -> PCA -> t-SNE
# ==========================================================

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from node2vec import Node2Vec
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# ==========================================================
# Create Knowledge Graph
# ==========================================================

G = nx.Graph()

edges = [

    # AI
    ("AI","Data Science"),
    ("AI","Data Engineering"),
    ("AI","Cloud"),

    # Data Science
    ("Data Science","Python"),
    ("Python","Pandas"),
    ("Python","NumPy"),
    ("Python","Scikit-Learn"),
    ("Python","Machine Learning"),
    ("Machine Learning","TensorFlow"),
    ("Machine Learning","PyTorch"),

    # Database
    ("Python","SQL"),
    ("SQL","MySQL"),
    ("SQL","Neo4j"),

    # Data Engineering
    ("Data Engineering","Apache Spark"),
    ("Apache Spark","Kafka"),
    ("Apache Spark","Hadoop"),

    # Cloud
    ("Cloud","AWS"),
    ("AWS","EC2"),
    ("AWS","S3"),
    ("AWS","Lambda"),

    # DevOps
    ("Cloud","Docker"),
    ("Docker","Git"),
    ("Docker","Kubernetes"),

    # Cross-domain links
    ("Python","Apache Spark"),
    ("Python","Docker"),
    ("Machine Learning","Apache Spark"),
    ("Machine Learning","AWS"),
    ("Neo4j","AI"),
    ("Kafka","AWS")

]

G.add_edges_from(edges)

print("Nodes :", G.number_of_nodes())
print("Edges :", G.number_of_edges())


# ==========================================================
# 1. Original Network Graph
# ==========================================================

plt.figure(figsize=(14,10))

pos = nx.spring_layout(
    G,
    seed=42,
    k=1.2
)

nx.draw_networkx_nodes(
    G,
    pos,
    node_size=1800,
    node_color="skyblue",
    edgecolors="black"
)

nx.draw_networkx_edges(
    G,
    pos,
    width=2
)

nx.draw_networkx_labels(
    G,
    pos,
    font_size=9,
    font_weight="bold"
)

plt.title("Knowledge Graph (24 Nodes)")
plt.axis("off")


# ==========================================================
# 2. Train Node2Vec
# ==========================================================

node2vec = Node2Vec(
    G,
    dimensions=16,
    walk_length=20,
    num_walks=100,
    workers=1,
    p=1,
    q=1,
    seed=42
)

model = node2vec.fit(
    window=5,
    min_count=1,
    sg=1,
    epochs=100
)

print("\nMost Similar to Python\n")
print(model.wv.most_similar("Python"))


# ==========================================================
# Get Embeddings
# ==========================================================

nodes = list(G.nodes())

embeddings = np.array([
    model.wv[node]
    for node in nodes
])


# ==========================================================
# 3. PCA Visualization
# ==========================================================

pca = PCA(n_components=2)

pca_points = pca.fit_transform(embeddings)

plt.figure(figsize=(12,8))

plt.scatter(
    pca_points[:,0],
    pca_points[:,1],
    s=280,
    edgecolors="black"
)

for i,node in enumerate(nodes):
    plt.text(
        pca_points[i,0]+0.02,
        pca_points[i,1]+0.02,
        node,
        fontsize=9
    )

plt.title("Node2Vec Embeddings (PCA)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(alpha=.3)

# plt.show()


# ==========================================================
# 4. t-SNE Visualization
# ==========================================================

tsne = TSNE(
    n_components=2,
    perplexity=3,
    init="random",
    learning_rate=50,
    random_state=42
)

tsne_points = tsne.fit_transform(embeddings)

plt.figure(figsize=(12,8))

plt.scatter(
    tsne_points[:,0],
    tsne_points[:,1],
    s=280,
    edgecolors="black"
)

for i,node in enumerate(nodes):
    plt.text(
        tsne_points[i,0]+0.5,
        tsne_points[i,1]+0.5,
        node,
        fontsize=9
    )

plt.title("Node2Vec Embeddings (t-SNE)")
plt.xlabel("t-SNE Dimension 1")
plt.ylabel("t-SNE Dimension 2")
plt.grid(alpha=.3)

plt.show()