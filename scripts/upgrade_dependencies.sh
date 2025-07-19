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
# TODO optionally delete virtualenv
###########################################
(
    set -e

    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

    if [[ "$(pyenv version-name)" == "lexicon" ]]; then
        pyenv deactivate lexicon
    fi

    if pyenv virtualenvs | grep -q "lexicon"; then
        pyenv uninstall lexicon
    fi

    pyenv virtualenv 3.9 lexicon




    pyenv activate lexicon

    if [[ "$(pyenv version-name)" != "lexicon" ]]; then
        echo "Error - lexicon virtualenv is not activated"
        exit 1
    fi
    pip install --upgrade pip
    pip install --upgrade pip-tools
    pip install --upgrade setuptools
    ###########################################
    # Upgrade python requirements/requirements-dev.txt
    # and requirements/requirements-prod.txt
    # Installs requirments-dev.txt
    ###########################################
    pip-compile requirements/requirements-prod.in
    pip-compile requirements/requirements-dev.in

    pip install --upgrade -r requirements/requirements-dev.txt
)