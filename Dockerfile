# 1. IMAGEN BASE (Python 3.12 igual que tu Colab)
FROM python:3.12-slim

# 2. DIRECTORIO DE TRABAJO
WORKDIR /app

# 3. INSTALAR LIBRERÍAS
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. COPIAR CÓDIGO
COPY . .

# 5. COMANDO DE ARRANQUE
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]