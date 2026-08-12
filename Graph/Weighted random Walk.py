import random
import networkx as nx

WG = nx.Graph()

WG.add_weighted_edges_from([
    ("Python","Pandas",10),
    ("Python","NumPy",9),
    ("Python","SQL",3),
    ("Python","Docker",1)
])


current = "Python"

neighbors = list(WG.neighbors(current))

weights = [
    WG[current][neighbor]["weight"]
    for neighbor in neighbors
]

print("Neighbors :", neighbors)
print("Weights :", weights)

next_node = random.choices(
    neighbors,
    weights=weights,
    k=1
)[0]

print("Next Node :", next_node)


def weighted_random_walk(graph, start_node, walk_length):

    walk = [start_node]
    current = start_node

    for _ in range(walk_length - 1):

        neighbors = list(graph.neighbors(current))

        if not neighbors:
            break

        weights = [
            graph[current][neighbor]["weight"]
            for neighbor in neighbors
        ]

        current = random.choices(
            neighbors,
            weights=weights,
            k=1
        )[0]

        walk.append(current)

    return walk

for i in range(10):
    print(weighted_random_walk(WG, "Python", 6))