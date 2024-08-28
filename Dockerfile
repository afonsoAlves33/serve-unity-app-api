FROM python:3.11.9-alpine
WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache gcc musl-dev \ 
    && apk update \
    && apk add g++ gcc make unixodbc-dev \
    && apk add curl \
    && curl https://download.microsoft.com/download/7/6/d/76de322a-d860-4894-9945-f0cc5d6a45f8/msodbcsql18_18.4.1.1-1_arm64.apk --output msodbcsql18_installer.apk \
    && apk add --no-cache --allow-untrusted msodbcsql18_installer.apk \
    && echo 'ignore this' \
    && rm msodbcsql18_installer.apk \
    && pip install --upgrade pip \
    && pip install -r requirements.txt 

COPY . .


ENV UVICORN_CMD="uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"

EXPOSE 8000

CMD ["sh", "-c", "$UVICORN_CMD"]