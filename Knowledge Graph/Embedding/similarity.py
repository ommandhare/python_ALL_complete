from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format(
    "kg_embeddings.txt",
    binary=False
)

print("Embeddings loaded!")

# print(len(model.index_to_key))

# print(model.index_to_key[:10])


node = model.index_to_key[11]

# print(node)

similar = model.most_similar(node, topn=10)

# print(similar)


import pandas as pd

nodes = pd.read_csv("nodes.csv")

mapping = dict(zip(nodes["elementId"], nodes["name"]))


node = model.index_to_key[0]

print("Query Node:", mapping.get(node, node))

for node_id, score in model.most_similar(node, topn=10):
    print(mapping.get(node_id, node_id), " ----- ", score)

