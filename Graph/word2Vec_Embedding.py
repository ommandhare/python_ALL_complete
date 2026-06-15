from gensim.models import Word2Vec

sentences = [
    ["python", "pandas", "numpy"],
    ["python", "pandas", "analysis"],
    ["python", "pandas", "data"],
    ["python", "numpy", "analysis"],
    ["sql", "database", "query"],
    ["sql", "database", "mysql"],
    ["sql", "query", "mysql"],
    ["database", "mysql", "query"]
]

model = Word2Vec(
    sentences,
    vector_size=10,
    window=2,
    min_count=1
)

print("Embedding....")
print(model.wv["sql"])

print("Most Similar...")
print(model.wv.most_similar("python",topn=3))