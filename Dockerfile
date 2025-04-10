# Этап 1: сборка
FROM python:3.13.2 as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Этап 2: финальный образ
FROM python:3.13.2-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
ENV PATH=/root/.local/bin:$PATH