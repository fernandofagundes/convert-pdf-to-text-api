# Imagem base com Python (pode ser ajustada para a versão desejada)
FROM python:3.9-slim

# Instala dependências do sistema necessárias para o pdf2image e OCR
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libsm6 \
    libxext6 \
    libxrender-dev \
    poppler-utils \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho na imagem
WORKDIR /app

# Copia o arquivo de dependências e instala as bibliotecas Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Expõe a porta que a aplicação usará
EXPOSE 8000

# Comando para iniciar a API com o Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
