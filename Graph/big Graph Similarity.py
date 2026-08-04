from node2vec import Node2Vec
import matplotlib.pyplot as plt
import networkx as nx
from pprint import pprint
G = nx.Graph()

edges = [

    # Programming
    ("Python","NumPy"),
    ("Python","Pandas"),
    ("Python","Scikit-Learn"),
    ("Python","TensorFlow"),
    ("Python","PyTorch"),
    ("Python","FastAPI"),
    ("Python","Flask"),

    # Data Science
    ("NumPy","Pandas"),
    ("Pandas","Matplotlib"),
    ("Pandas","Seaborn"),
    ("Scikit-Learn","Machine Learning"),
    ("TensorFlow","Deep Learning"),
    ("PyTorch","Deep Learning"),
    ("Machine Learning","Deep Learning"),
    ("Machine Learning","Statistics"),
    ("Machine Learning","Linear Algebra"),
    ("Machine Learning","Probability"),

    # Databases
    ("SQL","MySQL"),
    ("SQL","PostgreSQL"),
    ("SQL","Oracle"),
    ("SQL","SQLite"),
    ("SQL","Database"),
    ("Database","MongoDB"),
    ("Database","Neo4j"),
    ("Database","Redis"),

    # Data Engineering
    ("Python","Apache Spark"),
    ("Apache Spark","PySpark"),
    ("Apache Spark","Hadoop"),
    ("Apache Spark","Kafka"),
    ("Apache Spark","Airflow"),
    ("Airflow","ETL"),
    ("ETL","Data Engineering"),
    ("Data Engineering","BigQuery"),
    ("Data Engineering","Snowflake"),
    ("Data Engineering","AWS"),
    ("Data Engineering","Azure"),

    # Visualization
    ("Pandas","Power BI"),
    ("Pandas","Tableau"),
    ("Power BI","Excel"),
    ("Tableau","Excel"),

    # Version Control
    ("Python","Git"),
    ("Git","GitHub"),
    ("GitHub","Docker"),
    ("Docker","Kubernetes"),

    # Graph
    ("Python","NetworkX"),
    ("NetworkX","Graph Embedding"),
    ("Graph Embedding","Node2Vec"),
    ("Graph Embedding","DeepWalk"),
    ("Graph Embedding","Word2Vec"),
    ("Graph Embedding","Neo4j"),

    # AI
    ("Deep Learning", "Computer Vision"),
    ("Deep Learning","NLP"),
    ("NLP", "Transformers"),
    ("Transformers","LLM"),
    ("LLM", "OpenAI"),
    ("LLM", "LangChain"),
    ("LangChain","RAG"),
    ("RAG","Vector Database"),
    ("Vector Database","FAISS"),
    ("Vector Database","ChromaDB"),

    # Cloud
    ("AWS","S3"),
    ("AWS","EC2"),
    ("Azure","Azure Storage"),

    # User
    ("Om","Python"),
    ("Om","SQL"),
    ("Om","Power BI"),
    ("Om","Data Engineering"),
    ("Om","Graph Embedding"),
]

G.add_edges_from(edges)

# plt.figure(figsize=(14,10))
# pos = nx.spring_layout(G, seed=42, k=1)

#GRAPH PLOTTING
# nx.draw_networkx_nodes(
#     G, pos,
#     node_size=1600,
#     node_color="skyblue",
#     edgecolors="black"
# )
#
# nx.draw_networkx_edges(
#     G,
#     pos,
#     width=2
# )
#
# nx.draw_networkx_labels(
#     G,
#     pos,
#     font_size=10,
#     font_weight="bold"
# )
#
# plt.title("Original Knowledge Graph", fontsize=18)
# plt.axis("off")


print("Nodes :", G.number_of_nodes())
print("Edges :", G.number_of_edges())

node2vec = Node2Vec(
    G,
    dimensions=32,
    walk_length=30,
    num_walks=200,
    p=1,
    q=1,
    workers=1,
    seed=42
)

model = node2vec.fit(
    window=10,
    min_count=1,
    sg=1,
    epochs=100
)

print("---" * 30)
print("Similar to ")
pprint(model.wv.most_similar("LLM", topn=30))
print("---" * 30)
print(model.wv["LLM"])



# plt.show()