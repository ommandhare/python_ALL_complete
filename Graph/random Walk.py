import networkx as nx
import random
from gensim.models import Word2Vec

def random_walk(graph, start_node, walk_length):

    walk = [start_node]

    current = start_node

    for _ in range(walk_length - 1):

        neighbors = list(graph.neighbors(current))

        current = random.choice(neighbors)

        walk.append(current)

    return walk


G = nx.Graph()

G.add_edges_from([
     ("A","B"),
     ("B","C"),
     ("B","D")
])

# print(random_walk(G, "A", 5))


walks = []

for node in G.nodes():

    for _ in range(10):

        walk = random_walk(G, node, 5)

        walks.append(walk)


model = Word2Vec(
    walks,
    vector_size=16,
    window=3,
    min_count=1
)

print(model.wv["A"])
