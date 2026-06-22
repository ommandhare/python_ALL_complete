# Day 4 — Random Walks & DeepWalk

Today is the day where Graphs and Word2Vec finally connect together.

Yesterday you learned:

```text
Words
↓
Sentences
↓
Word2Vec
↓
Embeddings
```

Today's question:

> "Graphs don't have sentences, so how can we use Word2Vec on a graph?"

The answer is:

```text
Random Walks
```

---

# 1. What is a Random Walk?

Imagine this graph:

```text
A --- B --- C
      |
      |
      D
```

Start at:

```text
A
```

Move randomly to a neighbor.

Possible walk:

```text
A → B → D
```

Another walk:

```text
A → B → C
```

Another:

```text
D → B → A
```

Each walk becomes a "sentence".

---

# Graph vs NLP

NLP:

```text
Sentence:
Python Pandas NumPy
```

Graph:

```text
Walk:
A B D
```

Word2Vec doesn't care whether it's a sentence or a graph walk.

It only sees sequences.

---

# 2. Why Random Walks Work

Suppose:

```text
A --- B --- C
      |
      |
      D
```

Many walks will contain:

```text
A B
B C
B D
```

Word2Vec starts learning:

```text
A is close to B
C is close to B
D is close to B
```

because they frequently appear together.

---

# 3. Manual Example

Graph:

```text
A --- B --- C
      |
      |
      D
```

Generate walks:

```text
Walk 1:
A B C

Walk 2:
A B D

Walk 3:
D B C

Walk 4:
C B A
```

Treat as sentences:

```python
[
 ['A','B','C'],
 ['A','B','D'],
 ['D','B','C'],
 ['C','B','A']
]
```

Now Word2Vec can train.

---

# 4. DeepWalk

DeepWalk was the first major Graph Embedding algorithm.

Pipeline:

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

That's literally DeepWalk.

Nothing more.

---

# DeepWalk Architecture

```text
        Graph
          │
          ▼
   Random Walks
          │
          ▼
     Sentences
          │
          ▼
      Word2Vec
          │
          ▼
      Embeddings
```

---

# 5. Implement Random Walk

Create graph:

```python
import networkx as nx
import random

G = nx.Graph()

G.add_edges_from([
    ("A","B"),
    ("B","C"),
    ("B","D")
])
```

---

Random Walk Function:

```python
def random_walk(graph, start_node, walk_length):

    walk = [start_node]

    current = start_node

    for _ in range(walk_length - 1):

        neighbors = list(graph.neighbors(current))

        current = random.choice(neighbors)

        walk.append(current)

    return walk
```

---

Run:

```python
print(random_walk(G, "A", 5))
```

Possible output:

```python
['A', 'B', 'D', 'B', 'C']
```

Run again:

```python
['A', 'B', 'C', 'B', 'D']
```

Different every time.

---

# 6. Generate Many Walks

DeepWalk doesn't generate one walk.

It generates hundreds.

Example:

```python
walks = []

for node in G.nodes():

    for _ in range(10):

        walk = random_walk(G, node, 5)

        walks.append(walk)
```

Output:

```python
[
 ['A','B','D','B','C'],
 ['A','B','C','B','D'],
 ['B','C','B','A','B'],
 ...
]
```

These are now graph sentences.

---

# 7. Train Word2Vec on Walks

```python
from gensim.models import Word2Vec

model = Word2Vec(
    walks,
    vector_size=16,
    window=3,
    min_count=1
)
```

---

Get embedding:

```python
print(model.wv["A"])
```

Example:

```text
[0.23, -0.41, 0.18, ...]
```

---

Similarity:

```python
print(model.wv.most_similar("A"))
```

Example:

```text
[
 ('B',0.91),
 ('D',0.75),
 ('C',0.72)
]
```

---

# Why DeepWalk Works

Imagine:

```text
A --- B --- C
      |
      |
      D
```

Most walks contain:

```text
A and B
B and C
B and D
```

Word2Vec learns:

```text
B is central
```

and nearby nodes get similar vectors.

---

# Important Limitation of DeepWalk

DeepWalk always walks randomly.

It cannot decide:

```text
Stay local
```

or

```text
Explore far away
```

Everything is equally random.

This limitation led to:

```text
Node2Vec
```

which you'll learn tomorrow.

---

# Day 4 Assignment

## Part 1

Create graph:

```text
      A
     / \
    B   C
     \ /
      D
      |
      E
```

---

## Part 2

Write the random_walk() function.

---

## Part 3

Generate:

```python
20 walks
```

from every node.

---

## Part 4

Print first 10 walks.

Example:

```python
['A','B','D','E']
['C','D','B','A']
...
```

---

## Part 5

Train Word2Vec on those walks.

---

## Part 6

Print:

```python
model.wv.most_similar("A")
```

and

```python
model.wv.most_similar("D")
```

---

# Day 4 Notes Summary

```text
Graphs do not contain sentences
↓
Word2Vec needs sentences
↓
Random Walks create graph sentences
↓
Word2Vec trains on walks
↓
Node Embeddings are created
↓
This algorithm is called DeepWalk
```

When you finish the assignment, you'll already have built a simplified Graph Embedding system from scratch. Day 5 will then show how Node2Vec improves DeepWalk using the famous **p** and **q** parameters.