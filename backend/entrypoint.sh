#!/bin/bash

gunicorn backend.wsgi --name django_app --workers 1 --user=nobody --bind=127.0.0.1:8000 --daemon &&
/usr/sbin/nginx