import unittest
from unittest.mock import MagicMock, patch


class TestLexiconEntry(unittest.TestCase):

    def test_orchestrate_japanese_vocab(
            self
        ):
        """entry only invocation for creating japanese vocab"""
        from lexicon.entry.lexicon_entry import orchestrate_japanese_vocab

        orchestrate_japanese_vocab()

