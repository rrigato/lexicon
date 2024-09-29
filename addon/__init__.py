from aqt import mw
from aqt.qt import QMessageBox
from anki.hooks import addHook

def e2e_test_validation():
    QMessageBox.information(mw, "Validated Lexicon addon", "Hello from external")


addHook("profileLoaded", e2e_test_validation)
