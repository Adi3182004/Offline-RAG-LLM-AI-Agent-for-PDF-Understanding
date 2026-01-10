import easyocr
from pdf2image import convert_from_path
import numpy as np

reader = easyocr.Reader(['en'], gpu=False)

def pdf_to_text(pdf_path, output_path):
    images = convert_from_path(pdf_path, dpi=300)
    text = ""
    for img in images:
        img_np = np.array(img)
        result = reader.readtext(img_np, detail=0, paragraph=True)
        text += " ".join(result) + "\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
