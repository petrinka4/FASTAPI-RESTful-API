FROM python:3.13.2 as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt


FROM python:3.13.2-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
ENTRYPOINT ["sh", "./entrypoint.sh"]