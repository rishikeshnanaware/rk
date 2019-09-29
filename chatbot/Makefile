run:
	python manage.py runserver localhost:8000

req:
	@echo "Updating requirements"
	@pip freeze > requirements.txt

migrate:
	@echo 'Running migrations'
	@echo '------------------'
	python manage.py migrate