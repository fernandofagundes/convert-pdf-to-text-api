from flask import Flask, request, jsonify
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

app = Flask(__name__)


# Configura o caminho do executável do Tesseract, se necessário
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'erro': 'Arquivo não fornecido'}), 400

    pdf_file = request.files['file']
    if pdf_file.filename == '':
        return jsonify({'erro': 'Nenhum arquivo selecionado'}), 400

    try:
        file_bytes = pdf_file.read()
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        texto_extraido = ""

        for page in doc:
            image_list = page.get_images(full=True)
            page_text = page.get_text("text")

            if page_text.strip() == "":  # Se não houver texto, tenta OCR nas imagens
                for img_index, img in enumerate(image_list):
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    image = Image.open(io.BytesIO(image_bytes))
                    page_text += pytesseract.image_to_string(image, lang='por')

            texto_extraido += page_text

        return jsonify({'texto': texto_extraido}), 200

    except Exception as e:
        return jsonify({'erro': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
