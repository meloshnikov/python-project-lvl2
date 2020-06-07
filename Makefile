install:
	poetry install

lint:
	poetry run flake8 gendiff

build:
	poetry build

pub:
	poetry publish -r ppt