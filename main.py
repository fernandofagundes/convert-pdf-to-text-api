from fastapi import FastAPI, File, UploadFile, HTTPException
import tempfile
import os

from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pytesseract

app = FastAPI(title="API PDF para Texto")

def extrair_texto_pdf(file_path: str) -> str:
    """
    Tenta extrair texto do PDF usando PyPDF2.
    """
    texto = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            pagina_texto = page.extract_text()
            if pagina_texto:
                texto += pagina_texto + "\n"
    except Exception as e:
        print("Erro ao extrair texto com PyPDF2:", e)
    return texto

def extrair_texto_ocr(file_path: str) -> str:
    """
    Converte cada página do PDF em imagem e usa OCR para extrair o texto.
    """
    texto = ""
    try:
        imagens = convert_from_path(file_path)
        for imagem in imagens:
            texto += pytesseract.image_to_string(imagem) + "\n"
    except Exception as e:
        print("Erro ao extrair texto via OCR:", e)
    return texto

@app.post("/convert-pdf", summary="Converte um PDF em texto")
async def convert_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="O arquivo deve ser um PDF.")

    # Salva o arquivo PDF temporariamente
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        conteudo = await file.read()
        tmp.write(conteudo)
        caminho_pdf = tmp.name

    # Tenta extrair texto diretamente
    texto_extraido = extrair_texto_pdf(caminho_pdf)

    # Se o texto extraído estiver vazio, tenta usar OCR
    if not texto_extraido.strip():
        texto_extraido = extrair_texto_ocr(caminho_pdf)

    # Remove o arquivo temporário
    os.remove(caminho_pdf)

    return {"texto": texto_extraido}

@app.get("/status")
async def status_check():
    return {"status": "up"}

@app.get("/")
async def status_check():
    return {"status": "up"}