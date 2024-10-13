import logging
import os
from logging.handlers import RotatingFileHandler
from time import strftime

# import the main window object (mw) from aqt
from aqt import mw
from aqt.qt import QAction, QMessageBox
# import the "show info" tool from utils.py
from aqt.utils import qconnect


# from aqt.qt import debug;
# debug()
# TODO - Find the directory where the add-on is installed

addon_path = "."
# addon_path = mw.addonManager.getAddonDir("lexicon")



# lexicon_handler = RotatingFileHandler(filename=os.path.join(
#     "user_files",
#     "lexicon_addon.log"
#     ),
#     maxBytes=10000,
#     backupCount=3
# )
lexicon_handler = RotatingFileHandler(
    filename="/Users/ryan/Library/Application Support/Anki2/addons21/lexicon/user_files/lexicon_addon.log",
    maxBytes=10000,
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
logging.info(os.getcwd())

def e2e_test_validation():
    """End to end test for validation"""
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
