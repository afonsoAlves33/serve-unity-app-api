FROM python:3.11.9-alpine
WORKDIR /app

COPY requirements.txt .
RUN apk add --no-cache gcc musl-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt
COPY . .

ENV UVICORN_CMD="uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"

EXPOSE 8000

CMD ["sh", "-c", "$UVICORN_CMD"]