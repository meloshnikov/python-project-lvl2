install:
	poetry install

lint:
	poetry run flake8 gendiff

build:
	poetry build

pub:
	poetry publish -r ppt

test:
	poetry run pytest --cov=gendiff tests/ --cov-report xml