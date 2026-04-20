FROM python:3.10-slim
WORKDIR /app
COPY core/infra/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "core/cli/main.py"]
