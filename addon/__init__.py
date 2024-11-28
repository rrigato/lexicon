import logging
import sys
from aqt import mw

from aqt.qt import QAction, QMessageBox, QInputDialog
from aqt.utils import qconnect
from lexicon.repo.lexicon_repo import set_logger

def e2e_test_validation():
    """End to end test for validation"""
    logging.info(mw.addonManager.addonsFolder(__name__))
    QMessageBox.information(mw, "Validated Lexicon addon", "Hello from external")
    logging.info("Validated Lexicon addon")

def get_user_input():
    """Get user input and display greeting"""
    logging.info("Lexicon input dialog")
    vocab_word, no_errors = QInputDialog.getText(
        mw, "Input Dialog", "Please enter the vocabulary word:"
    )

    if no_errors and vocab_word:  # Check if input was provided and OK was pressed
        logging.info(vocab_word)

'''
NOTE -
anki addons working directory is /
The following directory is included in the sys.path:
    - /Users/<mac_user>/Library/Application Support/Anki2/addons21

entry point is the __init__.py file in
/Users/<mac_user>/Library/Application Support/Anki2/addons21/<addon_name>
in this case
/Users/<mac_user>/Library/Application Support/Anki2/addons21/lexicon

This block is ignored when running tests
'''
if "unittest" not in sys.modules.keys():
    '''TODO - setup tox configuration and check for environment variable?'''
    set_logger()
    logging.info("Lexicon addon loaded")
    logging.debug("Lexicon addon debug loaded")
    action = QAction("lexicon", mw)
    # set it to call testFunction when it's clicked
    qconnect(action.triggered, e2e_test_validation)
    qconnect(action.triggered, get_user_input)
    # and add it to the tools menu
    mw.form.menuTools.addAction(action)
