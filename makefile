setup: pyproject.toml
	curl -sSL https://install.python-poetry.org | python3 -
	poetry env use python3
	poetry install --no-root

test:
	poetry run_tests
