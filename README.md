# README #

API em Python que recebe um arquivo PDF e tranforma em texto.
O arquivo PDF pode conter image ou o texto pode ser imagem que a API irá converter em texto.

Está API roda com um container docker

#### Cria o container localmente ####
```bash
docker build -t pdf-to-text-api .
```

#### Executa o container ####
```bash
docker run -d -p 8000:8000 pdf-to-text-api
```

A API estará disponível em [http://localhost:8000](http://localhost:8000). 

Você pode testar o endpoint /convert-pdf usando ferramentas como o Postman

[http://localhost:8000/convert-pdf](http://localhost:8000/convert-pdf).

Ou diretamente pela interface interativa do FastAPI em [http://localhost:8000/docs](http://localhost:8000/docs).