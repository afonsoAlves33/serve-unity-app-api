FROM python:3.11.9-alpine
WORKDIR /app

COPY requirements.txt .

RUN apk update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt 

COPY . .

EXPOSE 9000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--proxy-headers", "--port", "9000", "--reload"]