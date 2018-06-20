.PHONY: clean

clean:
	rm -f *.pyc
	rm -f tests/*.pyc
	rm -f src/*.pyc
	rm -rf __pycache__/
	rm -rf tests/__pycache__/
	rm -rf .pytest_cache/

