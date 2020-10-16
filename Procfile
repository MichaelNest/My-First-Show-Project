web: ( cd src && gunicorn core.wsgi:app --bind 0.0.0.0:$PORT )
release: python src/manage.py migrate