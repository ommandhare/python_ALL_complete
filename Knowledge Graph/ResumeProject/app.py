import DocumentLoader

loader = DocumentLoader("resume.pdf")

document = loader.load()

print(document["type"])
print(document["pages"])
print(document["needs_ocr"])
print(document["text"][:300])