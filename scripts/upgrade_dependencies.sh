set -e

pip install --upgrade pip
pip install --upgrade pip-tools
pip install --upgrade setuptools
###########################################
# Upgrade python requirements/requirements-dev.txt
# and requirements/requirements-prod.txt
# Installs requirments-dev.txt
# TODO - create fresh venv and install
###########################################
pip-compile requirements/requirements-prod.in
pip-compile requirements/requirements-dev.in

pip install --upgrade -r requirements/requirements-dev.txt