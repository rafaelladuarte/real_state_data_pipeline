FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends wget unzip

RUN apt-get update && apt-get install -y locales \
    && locale-gen pt_BR.UTF-8 \
    && echo "LANG=pt_BR.UTF-8" > /etc/default/locale \
    && echo "LC_ALL=pt_BR.UTF-8" >> /etc/default/locale \
    && echo "LC_TIME=pt_BR.UTF-8" >> /etc/default/locale \
    && apt-get clean

ENV LANG=pt_BR.UTF-8
ENV LC_ALL=pt_BR.UTF-8
ENV LC_TIME=pt_BR.UTF-8

WORKDIR /app

COPY .env /app/
COPY client_secrets.json /app/
COPY requirements.txt /app/

RUN mkdir -p /app/scripts
COPY . /app/scripts

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /app/venv \
    && /app/venv/bin/pip install --upgrade pip \
    && /app/venv/bin/pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

ENV PYTHONPATH=/app
ENV PATH="/app/venv/bin:$PATH"

CMD ["sh", "-c", "source /app/venv/bin/activate"]