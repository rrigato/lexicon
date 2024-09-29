import logging

# import the main window object (mw) from aqt
from aqt import mw
from aqt.qt import QAction, QMessageBox
# import the "show info" tool from utils.py
from aqt.utils import qconnect


logging.getLogger().setLevel(logging.INFO)

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
