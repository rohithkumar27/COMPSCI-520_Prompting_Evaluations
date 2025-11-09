# Makefile for Python project - similar to npm scripts
# Usage: make test, make coverage, make test-single, etc.

.PHONY: help install test coverage test-single test-all clean lint format

# Default target
help:
	@echo "Available commands (like npm run scripts):"
	@echo "  make install     - Install dependencies"
	@echo "  make test        - Run all tests"
	@echo "  make coverage    - Run tests with coverage"
	@echo "  make test-single - Run tests for single directory"
	@echo "  make test-all    - Run comprehensive test suite"
	@echo "  make clean       - Clean up generated files"
	@echo "  make lint        - Run code linting"
	@echo "  make format      - Format code with black"

# Install dependencies (like npm install)
install:
	pip install -r requirements.txt
	pip install -e .

# Run basic tests (like npm test)
test:
	pytest tests/ -v

# Run tests with coverage (like npm run test:coverage)
coverage:
	pytest --cov=generated --cov-report=html --cov-report=term-missing --cov-branch -v

# Run tests for a single directory
test-single:
	@echo "Testing multi_modal_simple directory..."
	cd generated/multi_modal_simple && python -m pytest test_*.py --cov=. --cov-report=term-missing -v

# Run all tests including generated solutions
test-all:
	@echo "Running comprehensive test suite..."
	python -m pytest generated/ --cov=generated --cov-report=html:coverage_html --cov-report=term-missing --cov-branch -v

# Clean up generated files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name "coverage_html*" -exec rm -rf {} +
	find . -name ".coverage" -delete

# Lint code
lint:
	flake8 generated/ tests/
	mypy generated/ --ignore-missing-imports

# Format code
format:
	black generated/ tests/