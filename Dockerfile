FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY cnnmodel.py .
COPY dataset_shard1.csv .
CMD ["python3", "cnnmodel.py"]