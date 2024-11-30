import logging
import os
import sys
from aqt import mw

from aqt.qt import QAction, QMessageBox, QInputDialog
from aqt.utils import qconnect

'''
Adds the third party dependencies to the python
runtime path.
refer to scripts/build_lexicon.sh for more on how third
parties are bundled
'''
try:
    from lexicon.repo.lexicon_repo import set_logger
except ModuleNotFoundError:
    os.sys.path.insert(
        0,
        os.path.join(
            mw.addonManager.addonsFolder("lexicon"),
            "third_party_dependencies"
        )
    )
    from lexicon.repo.lexicon_repo import set_logger

def e2e_test_validation():
    """End to end test for validation"""
    logging.info(mw.addonManager.addonsFolder(__name__))
    # QMessageBox.information(mw, "Validated Lexicon addon", "Hello from external")
    logging.info("Validated Lexicon addon")

def get_user_input():
    """Get user input and display greeting"""
    logging.info("Lexicon input dialog")
    vocab_word, no_errors = QInputDialog.getText(
        mw, "Input Dialog", "Please enter the vocabulary word:"
    )

    if no_errors and vocab_word:  # Check if input was provided and OK was pressed
        logging.info(vocab_word)
    from lexicon.entities.lexicon_entity_model import JapaneseVocabRequest
    from lexicon.repo.lexicon_repo import FlashCardRepo

    card_model_type, deck_to_insert_card = FlashCardRepo.create_audio_vocab_card(
        create_vocab_request=JapaneseVocabRequest(vocab_to_create=vocab_word)
    )

    logging.info(f"Card model type: {card_model_type}")
    logging.info(f"Deck to insert card: {deck_to_insert_card}")



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

    logging.info("addon.__init__.py - Lexicon addon loaded")
    logging.info("addon.__init__.py - sys.path: %s", sys.path)
    action = QAction("lexicon", mw)

    '''Note that qconnec
        is registering a slot that listens to emitted signals
    outside the flow of control of the the main thread'''
    qconnect(action.triggered, e2e_test_validation)
    qconnect(action.triggered, get_user_input)

    # add addon to the tools menu
    mw.form.menuTools.addAction(action)

    '''log any exceptions'''
    logging.exception("addon.__init__.py - unexpected error")
