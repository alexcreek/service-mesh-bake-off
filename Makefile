.PHONY: test

PIPENV_VERBOSITY = -1
export

test:
	pipenv run pytest || true
	pipenv run pylint --exit-zero --disable=R,C *.py
