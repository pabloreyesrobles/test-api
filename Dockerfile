FROM python:3.11

# setup timezone
RUN rm /etc/localtime && \
    echo 'America/Santiago' > /etc/timezone && \
    ln -s /usr/share/zoneinfo/America/Santiago /etc/localtime && \
    apt-get update && \
    apt-get install -q -y --no-install-recommends tzdata && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./app/* ./

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]