import logging
import os
from logging.handlers import RotatingFileHandler
import sys
from time import strftime
from lexicon.repo.lexicon_repo import set_logger

# import the main window object (mw) from aqt
from aqt import mw
from aqt.qt import QAction, QMessageBox
# import the "show info" tool from utils.py
from aqt.utils import qconnect
from pathlib import Path


lexicon_handler = RotatingFileHandler(
    filename=os.path.join(
        mw.addonManager.addonsFolder(__name__),
        "user_files",
        "lexicon_addon.log"
    ),
    maxBytes=3 * 1024 * 1024,
    backupCount=3
)


lexicon_handler.setFormatter(logging.Formatter(
            fmt="%(levelname)s | %(asctime)s.%(msecs)03d" +
            strftime("%z") + " | %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%S",
        )
)
lexicon_handler.setLevel(logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(lexicon_handler)

lexicon_handler = RotatingFileHandler(
    filename=os.path.join(
        mw.addonManager.addonsFolder(__name__),
        "user_files",
        "lexicon_addon.log"
    ),
    maxBytes=3 * 1024 * 1024,
    backupCount=3
)


lexicon_handler.setFormatter(logging.Formatter(
            fmt="%(levelname)s | %(asctime)s.%(msecs)03d" +
            strftime("%z") + " | %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%S",
        )
)
lexicon_handler.setLevel(logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(lexicon_handler)



def e2e_test_validation():
    """End to end test for validation"""
    logging.info(mw.addonManager.addonsFolder(__name__))
    QMessageBox.information(mw, "Validated Lexicon addon", "Hello from external")
    logging.info("Validated Lexicon addon")


def get_user_input():
    # Open a dialog box to get the user's name
    name, ok = QInputDialog.getText(mw, "Input Dialog", "Please enter your name:")

    if ok and name:  # Check if input was provided and OK was pressed
        show_greeting(name)



logging.info("Lexicon addon loaded")
logging.debug("Lexicon addon debug loaded")
action = QAction("lexicon", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, e2e_test_validation)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
'''
NOTE -
anki addons working directory is /
The following directory is included in the sys.path:
    - /Users/<mac_user>/Library/Application Support/Anki2/addons21

entry point is the __init__.py file in
/Users/<mac_user>/Library/Application Support/Anki2/addons21/<addon_name>
in this case
/Users/<mac_user>/Library/Application Support/Anki2/addons21/lexicon
'''