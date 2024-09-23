FROM python:3.11.9-alpine
WORKDIR /app

COPY requirements.txt .

RUN apk update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt 

COPY . .


ENV UVICORN_CMD="uvicorn app.main:app --host 0.0.0.0 --proxy-headers --port 8000"

EXPOSE 8000

CMD ["sh", "-c", "$UVICORN_CMD"]