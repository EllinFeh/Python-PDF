import fitz  
import pytesseract
from PIL import Image
import numpy as np
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_colored_text(image):
    img_array = np.array(image)
    
    text = pytesseract.image_to_string(img_array, config='--psm 6', lang='por')
    return text.strip()


def process_pdf(file_path):
   
    pdf_document = fitz.open(file_path)
    
    page = pdf_document[0]
    
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

     # Define as coordenadas para cortar a parte superior direita
    width, height = img.size
    # Ajuste os valores conforme necessário. Aqui, cortamos a metade direita e um quarto superior.
    left = width // 2
    upper = 0
    right = width
    lower = height // 4
    img_cropped = img.crop((left, upper, right, lower))
    
    extracted_text = extract_colored_text(img)
    
    pdf_document.close()
    
    return extracted_text

def rename_pdf(file_path, new_name):
    directory, _ = os.path.split(file_path)
    new_file_path = os.path.join(directory, new_name + ".pdf")
    os.rename(file_path, new_file_path)
    return new_file_path

pdf_path = "ES -8FI5.pdf"

extracted_text = process_pdf(pdf_path)

print(f"Texto extraído: {extracted_text}")

if extracted_text:
    new_pdf_path = rename_pdf(pdf_path, extracted_text)
    print(f"Arquivo renomeado para: {new_pdf_path} ")
else:
    print("Nenhum texto extraído para renomear o arquivo.")

