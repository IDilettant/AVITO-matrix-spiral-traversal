install:
		poetry install

lint:
	poetry run flake8 spiral_traversal/solution.py

isort:
	poetry run isort spiral_traversal tests

test:
	poetry run pytest

coverage:
	poetry run pytest --cov=spiral_traversal --cov-report xml

mypy-check:
	poetry run mypy --namespace-packages tests spiral_traversal

pre-commit:
	poetry run pre-commit run spiral_traversal


.PHONY: test, isort, coverage
