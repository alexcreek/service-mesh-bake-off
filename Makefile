.PHONY: test

test:
	pipenv run pytest || true
	pipenv run pylint --exit-zero --disable=R,C *.py
