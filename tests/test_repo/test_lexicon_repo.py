import unittest
from unittest.mock import MagicMock, patch

from lexicon.entities.lexicon_entity_model import AppConfig, FlashCard, JapaneseVocabRequest


class TestLexiconRepo(unittest.TestCase):

    @patch("lexicon.repo.lexicon_repo.FlashCardRepo.retrieve_app_config")
    @patch("lexicon.repo.lexicon_repo.mw")
    def test_create_audio_vocab_card(
        self,
        main_window_mock: MagicMock,
        retrieve_app_config_mock: MagicMock
    ):
        """Anki Note created"""
        from fixtures.lexicon_fixtures import mock_japanese_vocab_request
        from fixtures.lexicon_fixtures import mock_app_config
        from lexicon.repo.lexicon_repo import FlashCardRepo

        retrieve_app_config_mock.return_value = mock_app_config()
        main_window_mock.col.decks.by_name.return_value = {
            "id": 0
        }
        main_window_mock.col.new_note.return_value.id = 1
        main_window_mock.col.new_note.return_value.cards.return_value = [
            MagicMock(id=2)
        ]

        mock_created_flash_card = FlashCardRepo.create_audio_vocab_card(
            mock_app_config(),
            mock_japanese_vocab_request()
        )


        retrieve_app_config_mock.assert_not_called()
        main_window_mock.col.models.by_name.assert_called_once()
        main_window_mock.col.decks.by_name.assert_called_once()
        main_window_mock.col.new_note.assert_called_once()
        main_window_mock.col.add_note.assert_called_once()
        self.assertIsInstance(
            mock_created_flash_card,
            FlashCard
        )

    @patch("lexicon.repo.lexicon_repo.mw")
    def test_create_reading_vocab_card(
        self,
        main_window_mock: MagicMock
    ):
        """Anki reading Note created"""
        from fixtures.lexicon_fixtures import mock_japanese_vocab_request
        from fixtures.lexicon_fixtures import mock_app_config
        from lexicon.repo.lexicon_repo import FlashCardRepo

        main_window_mock.col.decks.by_name.return_value = {
            "id": 1
        }
        mock_runtime_config = mock_app_config()

        FlashCardRepo.create_reading_vocab_card(
            mock_japanese_vocab_request(),
            mock_runtime_config

        )

        main_window_mock.col.models.by_name.assert_called_once()
        main_window_mock.col.decks.by_name.assert_called_once()
        main_window_mock.col.new_note.assert_called_once()
        main_window_mock.col.add_note.assert_called_once()


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

        args, kwargs = rotating_file_handler_mock.call_args

        self.assertEqual(
            kwargs["encoding"],
            "utf-8",
            msg="e2e bug where not setting encoding cannot log non-ascii characters"
        )



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
        from lexicon.repo.lexicon_repo import FlashCardRepo

        self.assertEqual(
            FlashCardRepo.populate_hiragana_text(
                JapaneseVocabRequest(
                    vocab_to_create="輪廻"
                )
            ).hiragana_text,
            "りんね"
        )
        self.assertEqual(
            FlashCardRepo.populate_hiragana_text(
                JapaneseVocabRequest(
                    vocab_to_create="バッチリ"
                )
            ).hiragana_text,
            "ばっちり"
        )
        self.assertEqual(
            FlashCardRepo.populate_hiragana_text(
                JapaneseVocabRequest(
                    vocab_to_create="まったり"
                )
            ).hiragana_text,
            "まったり"
        )

    @patch("lexicon.repo.lexicon_repo.mw")
    def test_retrieve_app_config(
        self,
        main_window_mock: MagicMock
    ):
        """All properties of AppConfig are populated"""
        from fixtures.lexicon_fixtures import mock_japanese_vocab_request
        from lexicon.repo.lexicon_repo import FlashCardRepo

        main_window_mock.addonManager.getConfig.return_value = {
            "audio_vocab_deck_name": "mock_audio_vocab_deck_name",
            "audio_vocab_note_type": "mock_audio_vocab_note_type",
            "reading_vocab_deck_name": "mock_reading_vocab_deck_name",
            "reading_vocab_note_type": "mock_reading_vocab_note_type",
        }


        mock_app_config = FlashCardRepo.retrieve_app_config()


        [
            self.assertIsNotNone(
                getattr(mock_app_config, attr_name),
                msg=f"validate the following attribute is populated - {attr_name} "
            )
            for attr_name in dir(AppConfig)
            if not attr_name.startswith("_")

        ]