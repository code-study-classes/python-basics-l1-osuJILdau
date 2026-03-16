PYTHON ?= python3
TASKS = task_1.py task_2.py task_3.py task_4.py task_5.py

.PHONY: setup lint test check

setup:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install ruff pytest
	@if [ -d .git ]; then \
		mkdir -p .git/hooks; \
		printf '%s\n' '#!/bin/sh' 'make check' > .git/hooks/pre-push; \
		chmod +x .git/hooks/pre-push; \
		echo 'pre-push hook установлен'; \
	else \
		echo 'Папка .git не найдена, pre-push hook не установлен'; \
	fi

lint:
	$(PYTHON) -m ruff check $(TASKS)

test:
	$(PYTHON) -m pytest -q

check: lint test
