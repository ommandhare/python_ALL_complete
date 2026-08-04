from neo4j import GraphDatabase
import networkx as nx
from node2vec import Node2Vec

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "ommandhare1234"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))


query = """
MATCH (n)-[r]->(m)
RETURN
elementId(n) AS source,
labels(n) AS source_labels,
elementId(m) AS target,
labels(m) AS target_labels,
type(r) AS relationship
"""


with driver.session(database="conceptdictionary") as session:
    result = session.run(query)
    records = list(result)

# print(len(records))

# CREATING GRPAH IN NETWORK X

G = nx.Graph()

# Add all nodes first
with driver.session(database="conceptdictionary") as session:
    result = session.run("""
        MATCH (n)
        RETURN elementId(n) AS id
    """)

    for record in result:
        G.add_node(record["id"])

# Add edges
with driver.session(database="conceptdictionary") as session:
    result = session.run("""
        MATCH (n)-[r]->(m)
        RETURN
            elementId(n) AS source,
            elementId(m) AS target
    """)

    for record in result:
        G.add_edge(record["source"], record["target"])

print(G.number_of_nodes())  # Should be 4841
print(G.number_of_edges())  # Should be 7844


node2vec = Node2Vec(
    G,
    dimensions=16,
    walk_length=40,
    num_walks=300,
    p=1,
    q=1,
    workers=4,
    seed=42
)


model = node2vec.fit(
    window=10,
    min_count=1,
    batch_words=64
)

print(model.wv["Python"])
# model.wv.save_word2vec_format("kg_embeddings.txt")