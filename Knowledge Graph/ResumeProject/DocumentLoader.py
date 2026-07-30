from pathlib import Path
from typing import Dict, List

import fitz
import pdfplumber
from PIL import Image
from docx import Document


SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".png",
    ".jpg",
    ".jpeg",
    ".tiff",
    ".bmp"
}


class DocumentLoader:

    def __init__(self, file_path: str):

        self.file_path = Path(file_path)

        if not self.file_path.exists():
            raise FileNotFoundError(file_path)

        if self.file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            raise ValueError("Unsupported file")

    #######################################################

    def load(self):

        suffix = self.file_path.suffix.lower()

        if suffix == ".pdf":
            return self.load_pdf()

        elif suffix == ".docx":
            return self.load_docx()

        else:
            return self.load_image()

    #######################################################

    def load_docx(self):

        doc = Document(self.file_path)

        text = "\n".join(
            p.text for p in doc.paragraphs
        )

        return {

            "type": "docx",
            "pages": 1,
            "text": text,
            "needs_ocr": False,
            "images": []
        }

    #######################################################

    def load_image(self):

        img = Image.open(self.file_path)

        return {

            "type": "image",
            "pages": 1,
            "text": "",
            "needs_ocr": True,
            "images": [img]
        }

    #######################################################

    def load_pdf(self):

        doc = fitz.open(self.file_path)

        pdf_text = ""

        images = []

        for page in doc:

            pdf_text += page.get_text()

            pix = page.get_pixmap(dpi=300)

            img = Image.frombytes(
                "RGB",
                [pix.width, pix.height],
                pix.samples
            )

            images.append(img)

        needs_ocr = len(pdf_text.strip()) == 0

        return {

            "type": "pdf",
            "pages": len(doc),
            "text": pdf_text,
            "needs_ocr": needs_ocr,
            "images": images
        }