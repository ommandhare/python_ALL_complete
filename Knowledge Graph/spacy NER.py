import spacy
from docx import Document
file_path=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Knowledge Graph\resumes\OmMandhareResume.docx"

nlp = spacy.load("en_core_web_sm")

def read_docx(file_path):
    doc = Document(file_path)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text

text=read_docx(file_path)


# text = """
# # John Smith
# # Software Engineer at Google
# # Email: john@gmail.com
# # Worked at Microsoft from Jan 2021 to Mar 2023.
# # Lives in Bangalore.
# # """

doc = nlp(text)

for ent in doc.ents:
    print(f"{ent.text:30} -> {ent.label_}")