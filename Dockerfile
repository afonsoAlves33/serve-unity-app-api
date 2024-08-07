FROM python:3.11.9-alpine
WORKDIR /app
COPY requirements.txt .
RUN apk add --no-cache gcc musl-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
EXPOSE 3000