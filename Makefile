.PHONY: deploy debug install test

# Default path for the dylib file
DYLIB_PATH ?= /Applications/Anki.app/Contents/MacOS/libankihelper.dylib


deploy:
	./scripts/lexicon_local_deploy.sh

debug:
	./scripts/build_and_run_lexicon_locally.sh

# upgrades and installs dependencies for application
install:
	@echo "Upgrading and installing requirements..."
	./scripts/upgrade_dependencies.sh


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
