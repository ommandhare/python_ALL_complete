import networkx as nx
from node2vec import Node2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

def find_similar(node_name):

    print(f"\nTop Similar Nodes to {node_name}")

    for node,score in model.wv.most_similar(node_name):

        print(
            f"{node:<20} {score:.4f}"
        )






G = nx.Graph()

G.add_edges_from([
    ("Om", "Python"),
    ("Om", "SQL"),
    ("Om", "Pandas"),
    ("Rahul", "Pandas"),
    ("Rahul", "MachineLearning"),
    ("Amit", "SQL"),
    ("Amit", "Database"),
    ("Priya", "MachineLearning"),
    ("Priya", "Python"),
    ("Database", "SQL")
])

print("Nodes:")
print(list(G.nodes()))

print("\nEdges:")
print(list(G.edges()))


node2vec = Node2Vec(
    G,
    dimensions=64,
    walk_length=20,
    num_walks=100,
    workers=2
)

model = node2vec.fit(
    window=5,
    min_count=1
)

print("Example Embeddings ......")
print(model.wv["Python"])


print("Similar Nodes .......")
print(model.wv.most_similar("Om"))



print("Cosine Similarity score between tow Nodes.....")



vec1 = model.wv["Om"].reshape(1, -1)
vec2 = model.wv["Rahul"].reshape(1, -1)

score = cosine_similarity(vec1, vec2)

print(score)

print("Creating embedding Dataframe")

nodes = model.wv.index_to_key

embeddings = pd.DataFrame(
    model.wv.vectors,
    index=nodes
)

print(embeddings.head())


print("Creating Kmeans Cluster....")

kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

clusters = kmeans.fit_predict(
    model.wv.vectors
)

result = pd.DataFrame({
    "Node": model.wv.index_to_key,
    "Cluster": clusters
})

print(result.sort_values("Cluster"))


# print("PCA Reduction....")
#
# pca = PCA(
#     n_components=2
# )
#
# pca_result = pca.fit_transform(
#     model.wv.vectors
# )
#
# plt.figure(figsize=(10,6))
#
# plt.scatter(
#     pca_result[:,0],
#     pca_result[:,1]
# )
#
# for i,node in enumerate(model.wv.index_to_key):
#     plt.annotate(
#         node,
#         (
#             pca_result[i,0],
#             pca_result[i,1]
#         )
#     )
#
# plt.title("PCA Graph Embeddings")
# plt.show()


print("T-SNE Graph VISUALIZATION")


tsne = TSNE(
    n_components=2,
    perplexity=5,
    random_state=42
)

tsne_result = tsne.fit_transform(
    model.wv.vectors
)

print("Plotting T-SNE....")
plt.figure(figsize=(10,6))

plt.scatter(
    tsne_result[:,0],
    tsne_result[:,1]
)

for i,node in enumerate(model.wv.index_to_key):
    plt.annotate(
        node,
        (
            tsne_result[i,0],
            tsne_result[i,1]
        )
    )

plt.title("Graph Embeddings")



print("Find Similar Nodes...")
find_similar("Om")
find_similar("SQL")

plt.show()