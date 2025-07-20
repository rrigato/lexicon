#!/bin/bash

###########################################
# Upgrade python dependencies
# 1. Deactivate any existing lexicon virtualenv
# 2. Uninstall any existing lexicon virtualenv
# 3. Create a new lexicon virtualenv
# 4. Upgrade pip
# 5. Upgrade pip-tools
# 6. Upgrade setuptools
# 7. Upgrade requirements/requirements-prod.txt
# 8. Upgrade requirements/requirements-dev.txt
###########################################

set -e

# Constants
PYTHON_VERSION="3.9"
VIRTUALENV_NAME="lexicon"

init_pyenv() {
    echo "Initializing pyenv environment..."
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
}

deactivate_lexicon() {
    echo "Checking if lexicon virtualenv is active..."
    if [[ "$(pyenv version-name)" == "$VIRTUALENV_NAME" ]]; then
        echo "Deactivating lexicon virtualenv..."
        pyenv deactivate "$VIRTUALENV_NAME"
    fi
}

remove_existing_lexicon() {
    echo "Checking for existing lexicon virtualenv..."
    if pyenv virtualenvs | grep -q "$VIRTUALENV_NAME"; then
        echo "Removing existing lexicon virtualenv..."
        pyenv uninstall "$VIRTUALENV_NAME"
    fi
}

create_lexicon_virtualenv() {
    echo "Creating new lexicon virtualenv with Python $PYTHON_VERSION..."
    pyenv virtualenv "$PYTHON_VERSION" "$VIRTUALENV_NAME"
}

activate_lexicon() {
    echo "Activating lexicon virtualenv..."
    pyenv activate "$VIRTUALENV_NAME"

    if [[ "$(pyenv version-name)" != "$VIRTUALENV_NAME" ]]; then
        echo "Error - lexicon virtualenv is not activated"
        exit 1
    fi
    echo "Lexicon virtualenv activated successfully"
}

upgrade_core_tools() {
    echo "Upgrading core pip tools..."
    pip install --upgrade pip
    pip install --upgrade pip-tools
    pip install --upgrade setuptools
}

upgrade_requirements() {
    echo "Compiling and upgrading requirements..."
    pip-compile requirements/requirements-prod.in
    pip-compile requirements/requirements-dev.in
    pip install --upgrade -r requirements/requirements-dev.txt
}

main() {
    echo "Starting lexicon dependency upgrade process..."

    init_pyenv
    deactivate_lexicon
    remove_existing_lexicon
    create_lexicon_virtualenv
    activate_lexicon
    upgrade_core_tools
    upgrade_requirements

    echo "Lexicon dependency upgrade completed successfully!"
}

# Execute main function in subshell to prevent crashing parent shell
(
    main "$@"
)