import pandas as pd

txt_file = "kg_embeddings.txt"      # Your Node2Vec output file
csv_file = "KG_Node2Vec.csv"

rows = []

with open(txt_file, "r", encoding="utf-8") as f:
    # Skip the first line (e.g., "4830 128")
    next(f)

    for line in f:
        parts = line.strip().split()

        node_id = parts[0]
        embedding = [float(x) for x in parts[1:]]

        row = {"elementId": node_id}

        # Create one column per embedding dimension
        for i, value in enumerate(embedding):
            row[f"dim_{i+1}"] = value

        rows.append(row)

df = pd.DataFrame(rows)

df.to_csv(csv_file, index=False)

print(df.head())
print(f"Saved {len(df)} embeddings to {csv_file}")