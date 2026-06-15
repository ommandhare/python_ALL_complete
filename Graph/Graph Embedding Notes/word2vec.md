# Day 3 Notes – Word2Vec Foundations for Graph Embeddings

---

# Day 3 Objective

Understand:

```text
Why Embeddings Exist
↓
What Word2Vec Does
↓
How Similarity is Learned
↓
Why Graph Embeddings Use Word2Vec
```

---

# 1. Problem: Machine Learning Needs Numbers

Machine Learning cannot understand:

```text
Python
SQL
Pandas
```

It expects:

```python
[0.12, 0.55, 0.91]
```

numerical vectors.

---

# 2. One-Hot Encoding

Traditional approach:

| Word   | Vector  |
| ------ | ------- |
| Python | [1,0,0] |
| SQL    | [0,1,0] |
| Pandas | [0,0,1] |

---

## Problem

All words are equally distant.

```text
Python ↔ SQL
Python ↔ Pandas
Python ↔ Photoshop
```

Machine Learning cannot understand which words are related.

---

# 3. Embeddings

Embedding = Dense numerical representation of an object.

Example:

```text
Python → [0.12, 0.45, 0.88]

Pandas → [0.14, 0.42, 0.85]

SQL → [0.91, 0.22, 0.13]
```

Notice:

```text
Python ≈ Pandas
```

because their vectors are close.

---

# Definition

> An Embedding is a low-dimensional vector representation that captures semantic or structural similarity between objects.

---

# 4. What is Word2Vec?

Word2Vec is an algorithm developed by Google.

Purpose:

```text
Words
↓
Vectors
```

Example:

```text
King
Queen
Prince
Princess
```

↓

```text
King     → [0.41, 0.82]

Queen    → [0.40, 0.81]

Prince   → [0.52, 0.74]

Princess → [0.51, 0.73]
```

Similar words get similar vectors.

---

# 5. Main Idea of Word2Vec

Very Important:

> Words appearing in similar contexts should have similar vectors.

---

Example:

Sentence:

```text
Python works with Pandas
```

Python appears near:

```text
works
Pandas
```

---

Sentence:

```text
SQL works with Database
```

SQL appears near:

```text
works
Database
```

---

Word2Vec learns:

```text
Python ≈ SQL
```

because their surrounding words are similar.

---

# 6. Context Window

Sentence:

```text
Python Pandas NumPy
```

Window Size = 1

For:

```text
Pandas
```

Context is:

```text
Python
NumPy
```

---

Larger Window:

```python
window = 2
```

More surrounding words are considered.

---

# 7. Word2Vec Workflow

```text
Sentences
↓
Context Extraction
↓
Neural Network Training
↓
Embeddings
```

---

# 8. Gensim Implementation

Install:

```bash
pip install gensim
```

---

Example:

```python
from gensim.models import Word2Vec

sentences = [
    ["python", "pandas", "numpy"],
    ["python", "sql", "database"],
    ["python", "pandas", "analysis"],
    ["sql", "database", "query"]
]

model = Word2Vec(
    sentences,
    vector_size=10,
    window=2,
    min_count=1
)
```

---

# 9. Getting Embeddings

```python
model.wv["python"]
```

Example Output:

```text
[0.12, -0.33, 0.45, ...]
```

This is the learned embedding vector.

---

# 10. Similarity Search

```python
model.wv.most_similar("python")
```

Example:

```text
[
 ('pandas', 0.82),
 ('analysis', 0.71),
 ('numpy', 0.65)
]
```

Meaning:

These words appeared in similar contexts.

---

# Important Observation

Small datasets give poor results.

Example:

```python
4 sentences
```

is too small.

Word2Vec usually learns from:

```text
Thousands
Millions
Billions
```

of sentences.

---

# 11. Why Word2Vec Matters for Graph Embeddings

Word2Vec expects:

```text
Words
inside
Sentences
```

Graphs contain:

```text
Nodes
inside
Graphs
```

No sentences exist.

So we need to create sentences from graphs.

---

# Bridge to Graph Embeddings

Graph:

```text
A --- B --- C
      |
      D
```

Random Walk:

```text
A B D
```

Another Walk:

```text
A B C
```

Another Walk:

```text
D B C
```

These become:

```text
Sentence 1: A B D

Sentence 2: A B C

Sentence 3: D B C
```

Now Word2Vec can be applied.

---

# Core Insight

NLP World:

```text
Words
↓
Sentences
↓
Word2Vec
↓
Embeddings
```

Graph World:

```text
Nodes
↓
Random Walks
↓
Word2Vec
↓
Embeddings
```

---

# Interview Questions

### Q1: What is an embedding?

A numerical vector representation of an object that captures similarity and meaning.

---

### Q2: What is Word2Vec?

An algorithm that converts words into dense vectors based on their surrounding context.

---

### Q3: What is the main assumption behind Word2Vec?

Words appearing in similar contexts should have similar embeddings.

---

### Q4: Why can't we directly use Word2Vec on graphs?

Because graphs do not contain sentences.

---

### Q5: How do graph embedding algorithms use Word2Vec?

They generate random walks from graphs, treat them as sentences, and then train Word2Vec on those walks.

---

# Day 3 Summary

```text
Machine Learning needs vectors
↓
Embeddings provide vectors
↓
Word2Vec learns embeddings from context
↓
Similar context → Similar vectors
↓
Graphs have no sentences
↓
Random Walks create sentences
↓
Word2Vec can now learn Node Embeddings
↓
Foundation of DeepWalk and Node2Vec
```

**Next Topic (Day 4): Random Walks + DeepWalk**

* Generate graph sentences
* Build first graph embedding pipeline
* Understand how DeepWalk works internally
* Prepare for Node2Vec on Day 5.
