Excellent. Day 2 is where Graphs start becoming interesting.

Yesterday you learned:

```text
Node
Edge
Degree
Path
Neighbor
```

Today we'll answer:

> "Which nodes are important?"

Because in a graph, not all nodes are equally valuable.

---

# Day 2 Goal

Learn these 4 concepts:

```text
1. Degree Centrality
2. Betweenness Centrality
3. Closeness Centrality
4. Connected Components
```

These are called **Graph Metrics**.

---

# Graph for Today's Examples

Create this graph:

```python
import networkx as nx

G = nx.Graph()

G.add_edges_from([
    ("A","B"),
    ("A","C"),
    ("B","D"),
    ("C","D"),
    ("D","E"),
    ("E","F")
])
```

Visualization:

```text
      A
     / \
    B   C
     \ /
      D
      |
      E
      |
      F
```

---

# 1. Degree Centrality

Question:

> Who has the most direct connections?

You already know Degree.

Degree Centrality is a normalized version.

---

Example:

```text
A -> 2 connections
D -> 3 connections
F -> 1 connection
```

Clearly:

```text
D
```

is more important.

---

Code:

```python
degree = nx.degree_centrality(G)

for node, score in degree.items():
    print(node, round(score,3))
```

---

Think of Degree Centrality as:

```text
Popularity Score
```

---

# 2. Betweenness Centrality

Most important metric for today.

Question:

> Who acts as a bridge?

Look:

```text
A
|\
| \
B  C
 \/
 D
 |
 E
 |
 F
```

To reach F:

```text
A -> D -> E -> F
```

Almost every route passes through:

```text
D
```

---

If D disappears:

```text
A B C
```

cannot reach

```text
E F
```

---

Code:

```python
bet = nx.betweenness_centrality(G)

for node, score in bet.items():
    print(node, round(score,3))
```

---

Expected Winner:

```text
D
```

---

Interpretation:

```text
Bridge Node
```

---

# 3. Closeness Centrality

Question:

> Who can reach everyone fastest?

---

Imagine:

```text
A
|
B
|
C
|
D
|
E
```

C is in the middle.

---

C reaches:

```text
A quickly
B quickly
D quickly
E quickly
```

---

Code:

```python
close = nx.closeness_centrality(G)

for node, score in close.items():
    print(node, round(score,3))
```

---

Interpretation:

```text
Accessibility Score
```

---

# 4. Connected Components

Question:

> How many separate groups exist?

Example:

```python
G = nx.Graph()

G.add_edges_from([
    ("A","B"),
    ("B","C"),
    ("D","E")
])
```

Graph:

```text
A-B-C

D-E
```

Two separate groups.

---

Code:

```python
components = list(nx.connected_components(G))

print(components)
```

Output:

```python
[{'A','B','C'},
 {'D','E'}]
```

---

# Why This Matters

Graph Embeddings later try to preserve:

```text
Important Nodes
Communities
Neighborhoods
Connections
```

When Node2Vec generates vectors:

```text
A -> [0.2,0.5,0.1]

B -> [0.3,0.4,0.2]
```

it is secretly preserving many of these graph properties.

So today you are learning:

```text
Graph Structure
```

Before learning:

```text
Graph Embeddings
```

---