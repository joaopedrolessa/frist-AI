```markdown
# Projeto de OCR com Tesseract e Python

Este projeto utiliza Tesseract OCR e Python para extrair texto de imagens. Ele processa todas as imagens em um diretório de entrada e salva o texto extraído em arquivos `.txt` em um diretório de saída.

## Requisitos

Para rodar este projeto, você precisará de:

- Python 3.x
- Bibliotecas Python: `Pillow` e `pytesseract`
- Tesseract OCR

## Instalação

### Passo 1: Instalar o Tesseract OCR

Baixe e instale o Tesseract OCR a partir do [site oficial](https://github.com/tesseract-ocr/tesseract). Após a instalação, verifique o caminho de instalação. Neste projeto, assumimos que o Tesseract está instalado em `C:\Program Files\Tesseract-OCR`.

### Passo 2: Instalar as bibliotecas Python

Instale as bibliotecas necessárias executando o seguinte comando:

```bash
pip install Pillow pytesseract
```

### Passo 3: Configurar o Tesseract OCR no projeto

No seu script Python, configure o caminho para o executável do Tesseract e o diretório de dados:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ['TESSDATA_PREFIX'] = r"C:\Program Files\Tesseract-OCR\tessdata"
```

## Uso

1. Coloque as imagens que deseja processar no diretório `input`.
2. Execute o script Python. Ele processará todas as imagens no diretório `input` e salvará os textos extraídos no diretório `output`.

```python
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
```

## Insights e Possibilidades

Durante o desenvolvimento deste projeto, alguns pontos interessantes foram aprendidos:

- A precisão do OCR pode variar significativamente dependendo da qualidade e tipo da imagem.
- O Tesseract oferece suporte para várias línguas, o que pode ser configurado facilmente ajustando o parâmetro `lang` na função `image_to_string`.
- O pré-processamento de imagens (como ajuste de contraste e remoção de ruído) pode melhorar a precisão do OCR.

Este projeto pode ser expandido para incluir funcionalidades adicionais, como:

- Suporte para outros formatos de saída, como PDF ou DOCX.
- Implementação de pré-processamento de imagens para melhorar a qualidade do OCR.
- Interface gráfica para facilitar o uso por pessoas não técnicas.

## Licença

Este projeto é licenciado sob os termos da [MIT License](#). Para mais informações, consulte o arquivo `LICENSE`.
```