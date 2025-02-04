# README #

API responsável por converter PDF para texto

### Instalação das dependencias ###
```
    pip install -r requirements.txt
```
ou
```
    pip install flask PyMuPDF
```
```
    pip install flask PyMuPDF
```
#### executar o projeto ####
```
    python app.py
```

### exemplo de requisição ###
```
    curl -X POST -F "file=@/path/to/pdf/file.pdf" http://localhost:5000/convert
```

### exemplo de resposta ###
```
    {
        "text": "Texto do PDF"
    }
```