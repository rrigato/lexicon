import unittest
from unittest.mock import MagicMock, patch


class TestLexiconRepo(unittest.TestCase):

    def test_create_audio_vocab_card(self):
        """audio vocab card created for FlashCard"""
        from fixtures.lexicon_fixtures import mock_flash_cards
        from lexicon.repo.lexicon_repo import create_audio_vocab_card


        create_audio_vocab_card(
            mock_flash_cards(3)
        )


    @patch("lexicon.repo.lexicon_repo.logging")
    @patch("lexicon.repo.lexicon_repo.mw")
    def test_set_logger(
        self,
        main_window_mock: MagicMock,
        logging_mock: MagicMock
        ):
        """outgoing logging setup called"""
        from lexicon.repo.lexicon_repo import set_logger

        set_logger()

        main_window_mock.addonManager.addonsFolder.assert_called_once()
        logging_mock.handlers.RotatingFileHandler.assert_called_once()