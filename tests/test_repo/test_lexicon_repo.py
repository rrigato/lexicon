import unittest
from unittest.mock import MagicMock, patch

from lexicon.entities.lexicon_entity_model import JapaneseVocabRequest


class TestLexiconRepo(unittest.TestCase):

    def test_create_audio_vocab_card(self):
        """audio vocab card created for FlashCard"""
        from fixtures.lexicon_fixtures import mock_flash_cards
        from lexicon.repo.lexicon_repo import create_audio_vocab_card


        create_audio_vocab_card(
            mock_flash_cards(3)
        )


    @patch("lexicon.repo.lexicon_repo.RotatingFileHandler")
    @patch("lexicon.repo.lexicon_repo.logging")
    @patch("lexicon.repo.lexicon_repo.mw")
    def test_set_logger(
        self,
        main_window_mock: MagicMock,
        logging_mock: MagicMock,
        rotating_file_handler_mock: MagicMock
        ):
        """outgoing logging setup called"""
        from lexicon.repo.lexicon_repo import set_logger

        set_logger()

        rotating_file_handler_mock.assert_called_once()



    def test_is_only_japanese_characters(self):
        """input text is japansesse"""
        from lexicon.repo.lexicon_repo import FlashCardRepo
        mock_input_texts = [
            {
                "mock_vocab_request": "輪廻",
                "expected_output": True
            },
            {
                "mock_vocab_request": "ちょっぴり",
                "expected_output": True
            },
            {
                "mock_vocab_request": "トントン",
                "expected_output": True
            },
            {
                "mock_vocab_request": "じゃねlater",
                "expected_output": False
            },
            {
                "mock_vocab_request": "hello world",
                "expected_output": False
            },

        ]
        for mock_input_text in mock_input_texts:
            with self.subTest(mock_input_text=mock_input_text):

                self.assertEqual(
                    FlashCardRepo.is_only_japanese_characters(
                        mock_input_text["mock_vocab_request"]
                    ),
                    mock_input_text["expected_output"],
                    msg=f"\n check when {mock_input_text['mock_vocab_request']} is passed to interface"
                )


    def test_populate_hiraragana_text(self):
        """hiragana text populated"""
        from lexicon.repo.lexicon_repo import FlashCardRepo

        mock_vocab_request = JapaneseVocabRequest()
        mock_vocab_request.kanji_text = "輪廻"

        vocab_request_with_hiragana = FlashCardRepo.populate_hiragana_text(mock_vocab_request)

        self.assertEqual(
            vocab_request_with_hiragana.hiragana_text,
            "りんね"
        )