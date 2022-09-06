lint:
	black .
	isort .
	flake8 . --ignore=E501

test:
	pytest tests -v
