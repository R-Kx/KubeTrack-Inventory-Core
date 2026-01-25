FROM python:3.11-slim AS builder

WORKDIR /app

ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


FROM builder AS final

WORKDIR /app

RUN useradd -m test_user

COPY --from=builder /install /usr/local
COPY . .

RUN chown -R test_user:test_user /app

EXPOSE 7000

USER test_user

ENV PYTHONPATH=/app

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "7000"]