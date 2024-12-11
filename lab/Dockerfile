FROM python:3.13-slim

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY main.py /app/main.py

WORKDIR /app

CMD ["python", "main.py"]