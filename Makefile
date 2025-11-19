run_linters:
	@echo "\n\n... Запускаем проверку линтеров ...\n\n"; \
	uv run ruff check src --output-format=concise --config=./pyproject.toml


run_mypy:
	@echo "\n\n... Запускаем проверку типов ...\n\n"; \
	uv run --frozen mypy . --config-file=./pyproject.toml


run_tests:
	@echo "\n\n... Запускаем тесты ...\n\n"; \
	cmd_pytest="uv run pytest ."; \
	eval $$cmd_pytest


check_all: run_linters run_mypy run_tests
