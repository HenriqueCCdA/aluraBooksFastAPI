.PHONY: fmt
fmt:
	poetry run black tests/ api/
	poetry run ruff check tests api --fix


.PHONY: linter
linter:
	poetry run ruff check tests api
