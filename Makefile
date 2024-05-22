.PHONY: all $(MAKECMDGOALS)

run:
	ifeq ($(strip $(FILENAME)),)
		$(error FILENAME is not set)
	endif
	ifeq ($(strip $(DUPLICATES)),)
		$(error DUPLICATES is not set)
	endif
	docker run --rm --volume `pwd`:/opt/app --env PYTHON_PATH=/opt/app -w /opt/app python:3.6-slim python3 main.py $(FILENAME) $(DUPLICATES)
