FROM python:3.11-slim

WORKDIR /ore

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /ore/requirements.txt

COPY ./ore/ .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
