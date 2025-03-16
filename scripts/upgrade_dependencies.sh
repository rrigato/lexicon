set -e
###########################################
# Upgrade python requirements/requirements-dev.txt
# and requirements/requirements-prod.txt
# Installs requirments-dev.txt
# TODO - create fresh venv and install
###########################################
pip-compile requirements/requirements-dev.in
pip-compile requirements/requirements-prod.in

pip install --upgrade -r requirements/requirements-dev.txt