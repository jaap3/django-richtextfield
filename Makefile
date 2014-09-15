.PHONY: test tests tox coverage lint

help:
	@echo "test - run tests quickly with the default Python and Django version"
	@echo "tox - run tests on all Python/Django versions with tox"
	@echo "coverage - check code coverage quickly with the default Python and Django version"
	@echo "lint - check style with flake8"

test: tests
tests:
	python manage.py test

tox:
	tox

coverage:
	coverage run --source djrichtextfield --branch manage.py test
	coverage report -m
	coverage html
	python -mwebbrowser htmlcov/index.html

lint:
	flake8 djrichtextfield testproject
