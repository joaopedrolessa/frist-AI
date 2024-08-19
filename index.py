import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

os.environ['TESSDATA_PREFIX'] = r"C:\Program Files\Tesseract-OCR\tessdata"

input_dir = 'input'
output_dir = 'output'

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        try:
            image_path = os.path.join(input_dir, filename)
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image, lang='por')
            output_file = os.path.join(output_dir, f'{os.path.splitext(filename)[0]}.txt')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Processado: {filename}")
        except Exception as e:
            print(f"Erro ao processar {filename}: {e}")

print("Processamento concluído!")


