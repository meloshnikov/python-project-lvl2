install:
	poetry install

import: install
	poetry add pytest-cov

lint:
	poetry run flake8 gendiff

build:
	poetry build

pub:
	poetry publish -r ppt

test:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

dt:
	poetry run pytest --cov=gendiff tests/ --cov-report term-missing 