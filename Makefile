.PHONY: install

# Default path for the dylib file
DYLIB_PATH ?= /Applications/Anki.app/Contents/MacOS/libankihelper.dylib

# Default path for the virtual environment
VENV_PATH ?= ~/.pyenv/versions/lexicon/lib/python3.9/site-packages/_aqt/data/lib/

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
