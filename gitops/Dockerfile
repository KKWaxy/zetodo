ARG PYTHON_TAG_VERSION=3.12.2-alpine3.19
ARG PROJECT_NAME=zetodo

FROM python:${PYTHON_TAG_VERSION} AS builder

LABEL author="Wilfried KOUASSI" email="zeflexcorp@gmail.com" organization="zeflexcorp"

ENV USER=zeuser

# ENV UID=0766
# ENV GID=0766

WORKDIR /usr/local/app

COPY ./zetodo .

RUN set -o pipefail\
    && PYTHONDONTWRITEBYTECODE=1\ 
    && PYTHONUNBUFFERED=1\
    && python -m pip install --no-cache-dir -r  ./${PROJECT_NAME}/requirements.txt\
    && rm -rf /var/lib/apt/lists/*

FROM builder AS deploy

RUN adduser --no-create-home --disabled-password  -s /usr/sbin/nologin ${USER}

HEALTHCHECK --interval=5s --timeout=15s --start-period=5s --retries=3 \
 CMD curl -f http://localhost:8000/ || exit 1

RUN python manage.py collectstatic

USER ${USER}

EXPOSE 8000

CMD [ "gunicorn","-b","0.0.0.0:8000", "starter.wsgi"]
