#!/bin/sh

echo ">> Running DB migration..."
flask db upgrade

echo ">> Starting Gunicorn..."
exec gunicorn "app:create_app()" --bind 0.0.0.0:8080
