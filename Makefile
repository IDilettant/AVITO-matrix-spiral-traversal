lint:
	poetry run flake8 spiral_traverse/solution.py

isort:
	poetry run isort spiral_traverse tests

test:
	poetry run pytest

coverage:
	poetry run pytest --cov=spiral_traverse --cov-report xml

mypy-check:
	poetry run mypy --namespace-packages tests spiral_traverse

pre-commit:
	poetry run pre-commit run spiral_traverse


.PHONY: test, isort, coverage
