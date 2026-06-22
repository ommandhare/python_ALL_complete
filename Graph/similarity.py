from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

A = np.array([[1,2,3]])
B = np.array([[1,2,3]])

print(cosine_similarity(A,B))
