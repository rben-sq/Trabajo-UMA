FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

ENV NLTK_DATA=/usr/share/nltk_data

RUN python nltk_download.py

EXPOSE 5013

CMD ["python", "app.py"]
