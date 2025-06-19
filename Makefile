.PHONY: deploy debug install test

# Default path for the dylib file
DYLIB_PATH ?= /Applications/Anki.app/Contents/MacOS/libankihelper.dylib

# Default path for the virtual environment
VENV_PATH ?= ~/.pyenv/versions/lexicon/lib/python3.9/site-packages/_aqt/data/lib/

deploy:
	./scripts/lexicon_local_deploy.sh

debug:
	./scripts/build_and_run_lexicon_locally.sh

# upgrades and installs dependencies for application
install:
	@if [ ! -f "$(DYLIB_PATH)" ]; then \
		echo "$(DYLIB_PATH) \n not a valid path to libankihelper.dylib file"; \
		exit 1; \
	fi; \

	@echo "Upgrading and installing requirements..."
	./scripts/upgrade_dependencies.sh


	echo "Copying dylib file from $(DYLIB_PATH)...";
	mkdir -p $(VENV_PATH);
	cp "$(DYLIB_PATH)" $(VENV_PATH);


test:
	@echo "Running unittests with pyenv initialization..."
	@( \
		set -e; \
		export PYENV_ROOT="$$HOME/.pyenv"; \
		export PATH="$$PYENV_ROOT/bin:$$PATH"; \
		eval "$$(pyenv init -)"; \
		pyenv shell lexicon; \
		python -m unittest; \
		echo "Tests completed successfully"; \
	)
