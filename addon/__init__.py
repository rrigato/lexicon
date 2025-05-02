import logging
import os
import sys
from typing import Optional
from aqt import mw

from aqt.qt import QAction, QInputDialog, QMessageBox
from aqt.utils import qconnect

def configure_runtime_path():
    """Adds the third party dependencies to the python
    runtime path.
    refer to scripts/build_lexicon.sh for more on how third
    parties are bundled
    """

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

configure_runtime_path()
from lexicon.repo.lexicon_repo import set_logger
from lexicon.entry.lexicon_entry import learn_japanese_word
from lexicon.repo.lexicon_repo import FlashCardRepo


def _get_vocab_word_and_definition()-> tuple[str, str]:
    logging.info(
        "_get_vocab_word_and_definition - Lexicon input dialog"
    )
    vocab_word, no_errors = QInputDialog.getText(
        mw, "Input Dialog", "Please enter the vocabulary word:"
    )

    if no_errors and vocab_word:  # Check if input was provided and OK was pressed
        logging.info(
            "_get_vocab_word_and_definition - vocab_word: %s",
            vocab_word
        )

    word_definition, no_errors = QInputDialog.getText(
        mw, "Input Dialog", "Please enter the word definition:"
    )

    if no_errors and word_definition:
        logging.info(
            "_get_vocab_word_and_definition - word_definition: %s",
            word_definition
        )

    return vocab_word, word_definition


def _flash_card_input_prequisites(
        vocab_word: str,
        word_definition: str
)-> tuple[str, str, Optional[str]]:
    if vocab_word == "":
        logging.info(
            "_flash_card_input_prequisites - vocab_word empty"
        )
        return (
            vocab_word,
            word_definition,
            "Vocab word empty - no flash card created"
        )
    if word_definition == "":
        logging.info(
            "_flash_card_input_prequisites - word_definition empty"
        )
        return (
            vocab_word,
            word_definition,
            "Word definition empty - no flash card created"
        )
    return vocab_word, word_definition, None

def main():
    """Get user input and display greeting"""
    vocab_word, word_definition = _get_vocab_word_and_definition()

    vocab_word, word_definition, bad_input = (
        _flash_card_input_prequisites(
            vocab_word=vocab_word,
            word_definition=word_definition
        )
    )

    if bad_input:
        logging.info(
            "main - bad_input: %s",
            bad_input
        )
        QMessageBox.information(
            mw, "Invalid Input", bad_input
        )
        return

    flash_card_creation_error_message = learn_japanese_word(
        input_for_creating_flashcard=vocab_word,
        japanese_word_plugin=FlashCardRepo,
        word_definition=word_definition
    )

    if flash_card_creation_error_message:
        QMessageBox.information(
            mw, "Invalid Input", flash_card_creation_error_message
        )


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

    '''CMD on mac
    adds a shortcut to run the addon
    '''
    action.setShortcut("Ctrl+Shift+L")

    '''Note that qconnect
        is registering a slot that listens to emitted signals
    outside the flow of control of the the main thread'''
    qconnect(action.triggered, main)

    # add addon to the tools menu
    mw.form.menuTools.addAction(action)

