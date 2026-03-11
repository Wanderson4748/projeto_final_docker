# Imagem leve para deploy rápido
FROM python:3.12-slim

# Diretorio de trabalho
WORKDIR /app

# Instalação de dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código
COPY . .

# Expõe a porta do Flask
EXPOSE 5000

# Execução
CMD ["python", "app.py"]