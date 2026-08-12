import networkx as nx
from node2vec import Node2Vec
from pprint import pprint
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

G = nx.Graph()


edges = [
    # ===================== Programming =====================
    ("Python","Pandas"),
    ("Python","NumPy"),
    ("Python","Matplotlib"),
    ("Python","Seaborn"),
    ("Python","Scikit-Learn"),
    ("Pandas","NumPy"),
    ("Pandas","Matplotlib"),
    ("NumPy","Scikit-Learn"),
    ("Matplotlib","Seaborn"),

    # ===================== Machine Learning =====================
    ("Machine Learning","TensorFlow"),
    ("Machine Learning","PyTorch"),
    ("Machine Learning","Keras"),
    ("Machine Learning","XGBoost"),
    ("Machine Learning","LightGBM"),
    ("TensorFlow","Keras"),
    ("PyTorch","TorchVision"),
    ("TensorFlow","PyTorch"),

    # ===================== Database =====================
    ("SQL","MySQL"),
    ("SQL","PostgreSQL"),
    ("SQL","SQLite"),
    ("SQL","Oracle"),
    ("MySQL","PostgreSQL"),
    ("MongoDB","Cassandra"),
    ("MongoDB","Redis"),

    # ===================== Data Engineering =====================
    ("Apache Spark","PySpark"),
    ("Apache Spark","Kafka"),
    ("Apache Spark","Hadoop"),
    ("Apache Spark","Airflow"),
    ("Kafka","Airflow"),
    ("Kafka","Hadoop"),
    ("PySpark","Airflow"),

    # ===================== Cloud =====================
    ("AWS","EC2"),
    ("AWS","S3"),
    ("AWS","Lambda"),
    ("AWS","RDS"),
    ("AWS","IAM"),
    ("EC2","S3"),
    ("Lambda","API Gateway"),

    # ===================== DevOps =====================
    ("Docker","Kubernetes"),
    ("Docker","Git"),
    ("Docker","GitHub"),
    ("Docker","Jenkins"),
    ("Docker","Terraform"),
    ("Git","GitHub"),
    ("Jenkins","Terraform"),

    # =====================================================
    # Cross Community Connections
    # =====================================================

    ("Python","Machine Learning"),
    ("Scikit-Learn","Machine Learning"),

    ("Python","SQL"),
    ("Python","Apache Spark"),
    ("Python","AWS"),
    ("Python","Docker"),

    ("TensorFlow","AWS"),
    ("PyTorch","AWS"),

    ("Apache Spark","AWS"),
    ("Apache Spark","SQL"),

    ("Docker","AWS"),
    ("Docker","Apache Spark"),

    ("Kafka","SQL"),
    ("Airflow","Python"),
]

G.add_edges_from(edges)

print(G.nodes())
print(G.edges())

plt.figure(figsize=(10,7))

pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=1500,
    node_color="yellow",
    edge_color="black"
)

plt.title("Unweighted Graph")

node2vec_unweighted = Node2Vec(
    G,
    dimensions=16,
    walk_length=10,
    num_walks=50,
    workers=1,
    seed=42
)

model_unweighted = node2vec_unweighted.fit(
    window=5,
    min_count=1,
    sg=1,
    epochs=50
)



WG = nx.Graph()


WG.add_weighted_edges_from(
[

    # ===================== Programming =====================
    ("Python","Pandas",120),
    ("Python","NumPy",98),
    ("Python","Matplotlib",95),
    ("Python","Seaborn",40),
    ("Python","Scikit-Learn",90),
    ("Pandas","NumPy",98),
    ("Pandas","Matplotlib",90),
    ("NumPy","Scikit-Learn",92),
    ("Matplotlib","Seaborn",100),

    # ===================== Machine Learning =====================
    ("Machine Learning","TensorFlow",100),
    ("Machine Learning","PyTorch",98),
    ("Machine Learning","Keras",95),
    ("Machine Learning","XGBoost",92),
    ("Machine Learning","LightGBM",80),
    ("TensorFlow","Keras",100),
    ("PyTorch","TorchVision",95),
    ("TensorFlow","PyTorch",85),

    # ===================== Database =====================
    ("SQL","MySQL",100),
    ("SQL","PostgreSQL",98),
    ("SQL","SQLite",95),
    ("SQL","Oracle",92),
    ("MySQL","PostgreSQL",90),
    ("MongoDB","Cassandra",95),
    ("MongoDB","Redis",90),

    # ===================== Data Engineering =====================
    ("Apache Spark","PySpark",100),
    ("Apache Spark","Kafka",98),
    ("Apache Spark","Hadoop",95),
    ("Apache Spark","Airflow",92),
    ("Kafka","Airflow",90),
    ("Kafka","Hadoop",88),
    ("PySpark","Airflow",90),

    # ===================== Cloud =====================
    ("AWS","EC2",100),
    ("AWS","S3",100),
    ("AWS","Lambda",98),
    ("AWS","RDS",95),
    ("AWS","IAM",95),
    ("EC2","S3",90),
    ("Lambda","API Gateway",95),

    # ===================== DevOps =====================
    ("Docker","Kubernetes",100),
    ("Docker","Git",98),
    ("Docker","GitHub",95),
    ("Docker","Jenkins",92),
    ("Docker","Terraform",90),
    ("Git","GitHub",100),
    ("Jenkins","Terraform",90),

    # =====================================================
    # Weak Cross Community Connections
    # =====================================================

    ("Python","Machine Learning",15),
    ("Scikit-Learn","Machine Learning",20),

    # ("Python","SQL",2),
    # ("Python","Apache Spark",2),
    # ("Python","AWS",2),
    # ("Python","Docker",1),

    ("TensorFlow","AWS",5),
    ("PyTorch","AWS",4),

    ("Apache Spark","AWS",5),
    ("Apache Spark","SQL",4),

    ("Docker","AWS",3),
    ("Docker","Apache Spark",2),

    ("Kafka","SQL",3),
    ("Airflow","Python",3),
]


)

plt.figure(figsize=(10,7))

pos = nx.spring_layout(
    WG,
    seed=42,
    k=5,
    iterations=400,
    weight=None
)

nx.draw(
    WG,
    pos,
    with_labels=True,
    node_size=1500,
    node_color="lightgreen",
    font_size=8
)

labels = nx.get_edge_attributes(WG,"weight")

nx.draw_networkx_edge_labels(
    WG,
    pos,
    edge_labels=labels
)


node2vec_weighted = Node2Vec(
    WG,
    dimensions=16,
    walk_length=10,
    num_walks=50,
    workers=1,
    seed=42,
    weight_key="weight"
)

model_weighted = node2vec_weighted.fit(
    window=5,
    min_count=1,
    sg=1,
    epochs=50
)


print("UNWEIGHTED")
pprint(model_unweighted.wv.most_similar("Python"))

print("--" * 30)

print("WEIGHTED")
pprint(model_weighted.wv.most_similar("Python"))


plt.title("Weighted Graph")


# Get embeddings
nodes = list(G.nodes())
embeddings = [model_weighted.wv[node] for node in nodes]

# PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(embeddings)

# Plot
plt.figure(figsize=(12, 9))

plt.scatter(
    pca_result[:,0],
    pca_result[:,1],
    s=100
)

for i, node in enumerate(nodes):
    plt.text(
        pca_result[i,0] + 0.01,
        pca_result[i,1] + 0.01,
        node,
        fontsize=10
    )

plt.title("Weighted Graph Embeddings (PCA)", fontsize=16)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)

plt.show()