ARG PYTHON_VERSION=3.12.2

FROM python:${PYTHON_VERSION}-alpine3.19 AS builder

LABEL author="Wilfried KOUASSI" email="zeflexcorp@gmail.com" organization="zeflexcorp"

ENV UID=0766
ENV GID=0766

RUN PYTHONDONTWRITEBYTECODE=1 && PYTHONUNBUFFERED=1

WORKDIR /usr/local/app

COPY . .

RUN set -o pipefail &&\
    python -m pip install --no-cache-dir -r  ./requirements.txt &&\
    rm -rf /var/lib/apt/lists/*

FROM builder as deploy

RUN useradd -g ${GID} -u ${UID} -M  -s /usr/sbin/nologin zeuser


EXPOSE 8000
