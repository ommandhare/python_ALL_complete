import networkx as nx
import matplotlib.pyplot as plt
import random
from gensim.models import Word2Vec
from sklearn.decomposition import PCA

def random_walk(graph, start_node, walk_length):

    walk = [start_node]

    current = start_node

    for i in range(walk_length - 1):

        neighbors = list(graph.neighbors(current))

        current = random.choice(neighbors)

        walk.append(current)

    return walk
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

print("Nodes:")
print(list(G.nodes()))

print("\nEdges:")
print(list(G.edges()))

print("-------------")

nx.draw(
    G,
    with_labels=True,
    node_size=2000,
    font_size=10
)

# plt.show()

walks = []

for node in G.nodes():

    for i in range(5):

        walk = random_walk(G, node, 10)

        walks.append(walk)

print("Generated Walks:\n")

for walk in walks:
    print(walk)



model = Word2Vec(

    sentences=walks,

    vector_size=16,

    window=5,

    min_count=1,

    workers=1,

    sg=1,

    seed=42

)
# [-0.24849646 -0.18475862]

# print(model.wv["Om"])

for node in G.nodes():

    print(node)

    print(model.wv[node])

    print("-"*50)

for node in G.nodes():

    print(node)

    print(model.wv[node])

    print("-"*50)


print(model.wv.most_similar("Om"))



plt.show()