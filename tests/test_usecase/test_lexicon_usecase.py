import unittest
from unittest.mock import MagicMock

from fixtures.lexicon_fixtures import mock_japanese_vocab_request
class TestLexiconRepo(unittest.TestCase):

    def test_learn_japanese_word(self):
        """audio and reading vocab card created """
        from lexicon.usecase.lexicon_usecase import learn_japanese_word

        mock_plugin = MagicMock()
        mock_plugin.is_only_japanese_characters.return_value = True
        mock_plugin.populate_hiragana_text.return_value = mock_japanese_vocab_request()

        new_word_learned = learn_japanese_word(
            "mock_input",
            mock_plugin
        )

        self.assertFalse(
            new_word_learned
        )
        mock_plugin.create_audio_vocab_card.assert_called()
        mock_plugin.create_reading_vocab_card.assert_called()
        self.assertEqual(
            mock_plugin.set_flash_card_due_date_in_embeded_application.call_count,
            2,
            msg="set_flash_card_due_date_in_embeded_application should be set for both audio and reading flash cards"
        )
