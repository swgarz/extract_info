import pytesseract
from pdf2image import convert_from_path

def extract_text_from_image_pdf(pdf_file):
    # Convierte el PDF a imágenes
    pages = convert_from_path(pdf_file, 300)
    text = ""

    # Procesa cada página usando OCR
    for page in pages:
        text += pytesseract.image_to_string(page)

    return text


pdf_file = '/home/daniel/Escritorio/15 SO-RCM-920-2023 SO-DAF.pdf'  # Reemplaza con la ruta de tu archivo PDF
extracted_text = extract_text_from_image_pdf(pdf_file)

# Guarda el texto extraído en un archivo
with open('texto_extraido_ocr.txt', 'w', encoding='utf-8') as file:
    file.write(extracted_text)

print("El texto ha sido guardado en 'texto_extraido_ocr.txt'")
