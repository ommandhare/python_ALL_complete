from docx import Document
import os
import pandas as pd

folder = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Knowledge Graph\word files"

words = []

for file in os.listdir(folder):
    if file.endswith(".docx"):
        doc = Document(os.path.join(folder, file))

        for para in doc.paragraphs:
            for word in para.text.split():
                words.append({
                    "File": file,
                    "Word": word
                })

df = pd.DataFrame(words)

df.to_csv("words.csv", index=False, encoding="utf-8-sig")