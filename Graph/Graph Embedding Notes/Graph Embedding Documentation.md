
# Graph Embedding: From Fundamentals to Visualization

---

# 1. Introduction to Graphs

## What is a Graph?

A graph is a data structure consisting of:

* Nodes (Vertices)
* Edges (Relationships)

Example:

```text
Person ---- Works At ---- Company
```

### Graph Terminology

* Node
* Edge
* Neighbor
* Degree
* Path
* Connected Component

### Types of Graphs

* Directed Graph
* Undirected Graph
* Weighted Graph
* Bipartite Graph

### Python Example

```python
import networkx as nx

G = nx.Graph()

G.add_edge("Om", "Python")

print(G.nodes())
print(G.edges())
```

---

# 2. Graph Analytics Fundamentals

Before Graph Embeddings, understand graph structure.

## Degree Centrality

Measures direct influence.

```python
nx.degree_centrality(G)
```

---

## Betweenness Centrality

Measures bridge nodes.

```python
nx.betweenness_centrality(G)
```

---

## Closeness Centrality

Measures how quickly a node can reach others.

```python
nx.closeness_centrality(G)
```

---

## Connected Components

Identifies separate communities.

```python
nx.connected_components(G)
```

---

# 3. Why Graph Embeddings Are Needed

Machine Learning requires numerical features.

Graphs contain:

```text
Nodes
Edges
Relationships
```

Machine Learning expects:

```python
[0.12, 0.44, 0.91]
```

Need a transformation:

```text
Graph
↓
Embedding
↓
Vector
```

---

# 4. Embeddings

## What is an Embedding?

An embedding is a dense vector representation that preserves similarity and structure.

Example:

```text
Python → [0.12, 0.44, 0.81]

Pandas → [0.13, 0.42, 0.79]
```

Similar entities receive similar vectors.

---

## Benefits

* Similarity Search
* Recommendation Systems
* Clustering
* Classification
* Link Prediction

---

# 5. Word2Vec Fundamentals

Graph Embeddings are heavily inspired by Word2Vec.

## Word2Vec Concept

Words appearing in similar contexts should have similar vectors.

Example:

```text
Python works with Pandas

SQL works with Database
```

Word2Vec learns semantic similarity.

---

## Word2Vec Workflow

```text
Sentences
↓
Context Window
↓
Neural Network
↓
Embeddings
```

---

## Example

```python
from gensim.models import Word2Vec

sentences = [
    ["python", "pandas", "numpy"],
    ["python", "sql", "database"]
]

model = Word2Vec(sentences)
```

---

# 6. Random Walks

Graphs do not contain sentences.

Word2Vec requires sentences.

Random Walks solve this problem.

---

## Example Graph

```text
A --- B --- C
      |
      D
```

Random Walk:

```text
A → B → D
```

Another:

```text
A → B → C
```

These walks become sentences.

---

## Python Implementation

```python
def random_walk(graph,start,length):
    ...
```

---

# 7. DeepWalk Algorithm

DeepWalk is the first major Graph Embedding algorithm.

---

## Workflow

```text
Graph
↓
Random Walks
↓
Sentences
↓
Word2Vec
↓
Node Embeddings
```

---

## Advantages

* Simple
* Effective
* Foundation of Graph Embeddings

---

## Limitations

Random walks are completely unbiased.

No control over exploration.

---

# 8. Node2Vec Algorithm

Node2Vec improves DeepWalk.

---

## Core Idea

Control random walks.

Parameters:

### p (Return Parameter)

Controls probability of returning.

### q (In-Out Parameter)

Controls exploration behavior.

---

## BFS-like Behavior

Large q

```text
Local exploration
```

Useful for:

* Community detection

---

## DFS-like Behavior

Small q

```text
Deep exploration
```

Useful for:

* Structural similarity

---

## Node2Vec Workflow

```text
Graph
↓
Biased Random Walks
↓
Word2Vec
↓
Embeddings
```

---

## Python Example

```python
from node2vec import Node2Vec

node2vec = Node2Vec(
    G,
    dimensions=64,
    walk_length=20,
    num_walks=100,
    p=1,
    q=0.5
)

model = node2vec.fit()
```

---

# 9. Generating Node Embeddings

Obtain vector representation.

```python
model.wv["Om"]
```

Example:

```text
[0.11, -0.22, 0.55, ...]
```

---

# 10. Similarity Search

Find structurally similar nodes.

```python
model.wv.most_similar("Om")
```

Example:

```text
Rahul
Python
Pandas
```

---

# 11. Cosine Similarity

Measures similarity between vectors.

Interpretation:

* 1 → Highly Similar
* 0 → Unrelated
* -1 → Opposite

Formula:

---

## Example

```python
from sklearn.metrics.pairwise import cosine_similarity
```

---

# 12. Clustering Graph Embeddings

Group similar nodes.

---

## KMeans Clustering

```python
from sklearn.cluster import KMeans

kmeans = KMeans(
    n_clusters=3
)
```

---

## Output

```text
Cluster 1
Python
Pandas

Cluster 2
SQL
Database
```

---

# 13. Dimensionality Reduction

Node2Vec often generates:

```text
64 Dimensions
128 Dimensions
256 Dimensions
```

Humans cannot visualize them.

Need dimensionality reduction.

---

# 14. PCA Visualization

Principal Component Analysis.

Converts:

```text
128D
↓
2D
```

---

## Example

```python
from sklearn.decomposition import PCA
```

---

## Benefits

* Fast
* Easy to interpret

---

# 15. t-SNE Visualization

Most popular embedding visualization technique.

Converts:

```text
128D
↓
2D
```

while preserving local neighborhoods.

---

## Example

```python
from sklearn.manifold import TSNE
```

---

## Benefits

* Better cluster separation
* Better visualization quality

---

# 16. Complete Graph Embedding Pipeline

```text
Raw Data
↓
Graph Construction
↓
Graph Analytics
↓
Random Walks
↓
DeepWalk / Node2Vec
↓
Embeddings
↓
Similarity Search
↓
Cosine Similarity
↓
Clustering
↓
PCA / t-SNE Visualization
↓
Business Insights
```