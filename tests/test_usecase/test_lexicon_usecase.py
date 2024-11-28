import unittest
from unittest.mock import MagicMock
class TestLexiconRepo(unittest.TestCase):

    def test_learn_japanese_word(self):
        """audio and reading vocab card created """
        from lexicon.usecase.lexicon_usecase import learn_japanese_word

        mock_plugin = MagicMock()
        mock_plugin.is_only_japanese_characters.return_value = False

        new_word_learned = learn_japanese_word(
            "mock_input",
            mock_plugin
        )

        self.assertFalse(
            new_word_learned
        )
