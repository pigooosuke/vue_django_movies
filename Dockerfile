# frontend
FROM node:8.16.0-alpine

WORKDIR /build/

RUN npm install -g yarn

COPY /frontend/ ./

# RUN set -x \
#   && yarn install \
#   && yarn build

RUN yarn install
RUN sed -i -e '50s/Object/any/g' /build/node_modules/vue-apollo/types/options.d.ts
RUN yarn build

# backend api
FROM python:3.7.3-alpine3.9

RUN apk add --update --no-cache \
        build-base \
        git \
        curl \
        bash \
        nginx

COPY backend_django/Pipfile backend_django/Pipfile.lock ./
RUN set -ex \
  && pip install pipenv \
  && pipenv install --system --deploy

# setup api server
ENV PYTHONUNBUFFERED 1
ADD backend_django /service/django/

ADD backend_django/config/nginx.conf /etc/nginx/

WORKDIR /service/django
# ENTRYPOINT ["/bin/bash"]
# CMD ["/service/django/entrypoint.sh"]
