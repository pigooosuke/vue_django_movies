# backend api
FROM python:3.7.3-alpine3.9

RUN apk add --update --no-cache \
        build-base \
        git \
        curl \
        bash \
        nginx

RUN pip3 install -U pip

COPY backend/Pipfile backend/Pipfile.lock ./
RUN set -ex \
  && pip install pipenv \
  && pipenv install --system --deploy

# setup api server
ENV PYTHONUNBUFFERED 1
ADD backend /service/django/

ADD backend/config/nginx.conf /etc/nginx/


WORKDIR /service/django
ENTRYPOINT ["/bin/bash"]
CMD ["/service/django/entrypoint.sh"]
