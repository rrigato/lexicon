import unittest
from unittest.mock import MagicMock

from fixtures.lexicon_fixtures import mock_japanese_vocab_request
class TestAddonInit(unittest.TestCase):

    @patch("addon.__init__")
    def test_main(
        self,
        mock_init_module
    ):
        """external plugin calles clean architecture"""
        from addon import main

        

        new_word_learned = main(
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
