from flask import Flask, request, jsonify
import fitz  # PyMuPDF

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_pdf():
    # Verifica se o arquivo foi enviado com a chave 'file'
    if 'file' not in request.files:
        return jsonify({'erro': 'Arquivo não fornecido'}), 400

    pdf_file = request.files['file']

    # Verifica se o nome do arquivo não está vazio
    if pdf_file.filename == '':
        return jsonify({'erro': 'Nenhum arquivo selecionado'}), 400

    try:
        # Lê o conteúdo do arquivo em bytes
        file_bytes = pdf_file.read()

        # Abre o PDF a partir do stream de bytes
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        texto_extraido = ""

        # Itera por todas as páginas e extrai o texto de cada uma
        for page in doc:
            # Utiliza o método get_text para extrair o texto da página
            texto_extraido += page.get_text("text")

        # Retorna o texto extraído em formato JSON
        return jsonify({'texto': texto_extraido}), 200

    except Exception as e:
        # Em caso de erro, retorna a mensagem de erro e status 500
        return jsonify({'erro': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
