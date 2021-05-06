run:
	poetry run python manage.py runserver

run_gunicorn:
	export DJANGO_SETTINGS_MODULE=hello_django.settings
	poetry run gunicorn hello_django.wsgi