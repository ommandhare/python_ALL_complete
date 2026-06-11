Perfect. Let's start with **Day 1: Graph Fundamentals + NetworkX**.

The goal of Day 1 is **not Graph Embeddings**.

The goal is:

> "Become comfortable thinking in graphs."

---

# What is a Graph?

A graph consists of:

### Nodes (Vertices)

These are entities.

Examples:

```text
Person
Company
Product
Skill
```

---

### Edges

These are relationships.

Examples:

```text
Works At
Knows
Purchased
Has Skill
```

---

Example:

```text
Om ---- Works At ---- Company A
```

Here:

* Om = Node
* Company A = Node
* Works At = Edge

---

# Real Example Using Your LinkedIn-Type Data

Suppose you have:

| Person | Company |
| ------ | ------- |
| Om     | TCS     |
| Rahul  | Infosys |
| Amit   | TCS     |

Graph:

```text
Om ------ TCS
Amit ---- TCS

Rahul --- Infosys
```

This is much more powerful than a table because relationships become visible.

---

# Types of Graphs

## Undirected Graph

```text
A ----- B
```

Meaning:

```text
A is connected to B
B is connected to A
```

Example:

* Friends

---

## Directed Graph

```text
A -----> B
```

Meaning:

```text
A follows B
```

but

```text
B may not follow A
```

Example:

* LinkedIn Follow
* Twitter Follow

---

# Degree

Degree = Number of connections

Example:

```text
     B
     |
D ---A--- C
```

A has:

```text
Degree = 3
```

because A connects to:

* B
* C
* D

---

# Path

A route between nodes.

Example:

```text
A ---- B ---- C ---- D
```

Path from A to D:

```text
A → B → C → D
```

Length = 3

---

# Connected Components

Example:

```text
A ---- B

C ---- D
```

Two separate groups.

These are called:

```text
Connected Components
```

---

# Your First NetworkX Program

Install:

```bash
pip install networkx matplotlib
```

---

Create Graph:

```python
import networkx as nx

G = nx.Graph()

G.add_node("Om")
G.add_node("Rahul")

G.add_edge("Om", "Rahul")

print(G.nodes())
print(G.edges())
```

Output:

```python
['Om', 'Rahul']

[('Om', 'Rahul')]
```

---

# Add Multiple Nodes

```python
import networkx as nx

G = nx.Graph()

G.add_edges_from([
    ("Om", "Rahul"),
    ("Om", "Amit"),
    ("Rahul", "Priya")
])

print(G.nodes())
print(G.edges())
```

---

# Visualize Graph

```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([
    ("Om", "Rahul"),
    ("Om", "Amit"),
    ("Rahul", "Priya")
])

nx.draw(
    G,
    with_labels=True
)

plt.show()
```

You'll see:

```text
       Priya
         |
       Rahul
       /
     Om
      |
    Amit
```

(approximately)

---

# Find Degree

```python
for node in G.nodes():
    print(node, G.degree(node))
```

Output:

```text
Om 2
Rahul 2
Amit 1
Priya 1
```

---

# Find Neighbors

```python
print(list(G.neighbors("Om")))
```

Output:

```python
['Rahul', 'Amit']
```

---

# Find Shortest Path

```python
path = nx.shortest_path(
    G,
    source="Amit",
    target="Priya"
)

print(path)
```

Output:

```python
['Amit', 'Om', 'Rahul', 'Priya']
```

---

# Day 1 Assignment

Create this graph:

```text
              Python
                |
                |
Om ----- SQL ---|
 |              |
 |
Pandas
 |
Rahul
```

Represent:

### Nodes

```text
Om
Rahul
Python
SQL
Pandas
```

### Relationships

```text
Om → Python
Om → SQL
Om → Pandas
Rahul → Pandas
```

Then:

### Task 1

Print all nodes.

---

### Task 2

Print all edges.

---

### Task 3

Print degree of every node.

---

### Task 4

Visualize graph.

---

### Task 5

Find neighbors of "Om".

---

Once you complete that assignment (or show me your code), we'll move to **Day 2: Graph Metrics and Graph Algorithms**, where you'll learn concepts like centrality, importance, and why some nodes matter more than others.
