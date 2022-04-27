PHONY: help lint format lint format check-format

# Help system from https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install required packages
	pip install -r requirements.txt

test: ## Run tests locally
	pytest test.py

lint: ## Run Python linters
	flake8 . --exclude ./venv
	pylint *.py 

check-format: ## Check Python code formatting
	black . --check

format: ## Format Python code
	black .
