from copy import deepcopy
import json
import unittest
from unittest.mock import MagicMock, patch
from fixtures.lexicon_fixtures import mock_japanese_vocab_request
from lexicon.repo.lexicon_repo import FlashCardRepo

from lexicon.entities.lexicon_entity_model import AppConfig, FlashCard, JapaneseVocabRequest


class TestLexiconRepo(unittest.TestCase):

    @patch("lexicon.repo.lexicon_repo.FlashCardRepo.make_mp3_for_anki")
    @patch("lexicon.repo.lexicon_repo.FlashCardRepo.retrieve_app_config")
    @patch("lexicon.repo.lexicon_repo.mw")
    def test_create_audio_vocab_card(
        self,
        main_window_mock: MagicMock,
        retrieve_app_config_mock: MagicMock,
        make_mp3_for_anki_mock: MagicMock
    ):
        """Anki Note created"""
        from fixtures.lexicon_fixtures import mock_japanese_vocab_request
        from fixtures.lexicon_fixtures import mock_app_config
        from lexicon.repo.lexicon_repo import FlashCardRepo

        stubbed_app_config = mock_app_config()

        stubbed_app_config.audio_vocab_card_audio_column_number = 4
        main_window_mock.col.new_note.return_value.fields = [""] * 10
        main_window_mock.col.decks.by_name.return_value = {
            "id": 0
        }
        main_window_mock.col.new_note.return_value.id = 1
        main_window_mock.col.new_note.return_value.cards.return_value = [
            MagicMock(id=2)
        ]


        mock_created_flash_card = FlashCardRepo.create_audio_vocab_card(
            deepcopy(stubbed_app_config),
            mock_japanese_vocab_request()
        )


        retrieve_app_config_mock.assert_not_called()
        make_mp3_for_anki_mock.assert_called_once()
        main_window_mock.col.models.by_name.assert_called_once()
        main_window_mock.col.decks.by_name.assert_called_once()
        main_window_mock.col.new_note.assert_called_once()
        args, kwargs = main_window_mock.col.add_note.call_args
        self.assertIn(
            "[sound:",
            args[0].fields[
                stubbed_app_config.audio_vocab_card_audio_column_number
            ],
            msg=(
                "\n\nsound reference should be in fields element - "
                f"{stubbed_app_config.audio_vocab_card_audio_column_number} - "

            )
        )

        self.assertIsInstance(
            mock_created_flash_card,
            FlashCard
        )

    @patch("lexicon.repo.lexicon_repo.FlashCardRepo.make_mp3_for_anki")
    @patch("lexicon.repo.lexicon_repo.mw")
    def test_create_reading_vocab_card(
        self,
        main_window_mock: MagicMock,
        make_mp3_for_anki_mock: MagicMock
    ):
        """Anki reading Note created"""
        from fixtures.lexicon_fixtures import mock_japanese_vocab_request
        from fixtures.lexicon_fixtures import mock_app_config
        from lexicon.repo.lexicon_repo import FlashCardRepo

        main_window_mock.col.decks.by_name.return_value = {
            "id": 1
        }
        mock_new_note = MagicMock(id=4)
        mock_new_note.cards.return_value = [
            MagicMock(id=3)
        ]
        main_window_mock.col.new_note.return_value = mock_new_note
        main_window_mock.col.new_note.return_value.fields = [""] * 10
        mock_runtime_config = mock_app_config()
        mock_runtime_config.reading_vocab_card_audio_column_number = 6

        mock_reading_vocab_card = FlashCardRepo.create_reading_vocab_card(
            mock_japanese_vocab_request(),
            mock_runtime_config

        )

        main_window_mock.col.models.by_name.assert_called_once()
        main_window_mock.col.decks.by_name.assert_called_once()
        main_window_mock.col.new_note.assert_called_once()
        main_window_mock.col.add_note.assert_called_once()
        self.assertEqual(
            mock_reading_vocab_card.anki_card_id,
            3
        )
        self.assertEqual(
            mock_reading_vocab_card.anki_note_id,
            4
        )
        args, kwargs = main_window_mock.col.add_note.call_args
        self.assertIn(
            "[sound:",
            args[0].fields[
                mock_runtime_config.reading_vocab_card_audio_column_number
            ],
            msg=(
                "\n\nsound reference should be in fields element - "
                f"{mock_runtime_config.reading_vocab_card_audio_column_number} - "

            )
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

    @patch("lexicon.repo.lexicon_repo.tempfile")
    @patch("lexicon.repo.lexicon_repo.gTTS")
    @patch("lexicon.repo.lexicon_repo.mw")
    def test_make_mp3_for_anki(
        self,
        main_window_mock: MagicMock,
        gtts_mock: MagicMock,
        tempfile_mock: MagicMock
        ):
        """
            GIVEN - a JapaneVocabRequest
            WHEN - the request is passed to make_mp3_for_anki
            THEN - the str path to the mp3 file is returned
        """
        from fixtures.lexicon_fixtures import mock_app_config
        from fixtures.lexicon_fixtures import mock_japanese_vocab_request
        from lexicon.repo.lexicon_repo import FlashCardRepo

        mock_mp3_path = "temporary/os/dir/駆逐.mp3"
        tempfile_mock.gettempdir.return_value = "temporary/os/dir"
        gtts_mock.return_value.save.return_value = None
        main_window_mock.col.media.add_file.return_value = mock_mp3_path

        self.assertEqual(
            FlashCardRepo.make_mp3_for_anki(
                mock_app_config(),
                mock_japanese_vocab_request()
            ),
            mock_mp3_path
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
        """All properties of AppConfig are populated
        and e2e test of config.json shipped with application"""

        with open("addon/config.json") as json_file:
            mock_dict_config = json.load(json_file)

        mock_dict_config["audio_vocab_card_due_date"] = 1
        mock_dict_config["reading_vocab_card_due_date"] = 2

        main_window_mock.addonManager.getConfig.return_value = mock_dict_config

        mock_app_config = FlashCardRepo.retrieve_app_config()

        [
            self.assertIsNotNone(
                getattr(mock_app_config, attr_name),
                msg=f"validate the following attribute is populated - {attr_name} "
            )
            for attr_name in dir(AppConfig)
            if not attr_name.startswith("_")

        ]

    @patch("lexicon.repo.lexicon_repo.reading_column_selector")
    @patch("lexicon.repo.lexicon_repo.audio_column_selector")
    @patch("lexicon.repo.lexicon_repo.mw")
    def test_retrieve_app_config_audio_and_reading_column_selectors_called(
        self,
        main_window_mock: MagicMock,
        audio_column_selector_mock: MagicMock,
        reading_column_selector_mock: MagicMock,
        ):
        """
        GIVEN -
        - a valid config.json
        WHEN -
        - the retrieve_app_config method is called
        THEN -
        - the audio_column_selector and reading_column_selector methods are called
        """
        with open("addon/config.json") as json_file:
            mock_dict_config = json.load(json_file)

        main_window_mock.addonManager.getConfig.return_value = mock_dict_config
        audio_column_selector_mock.return_value = 2
        reading_column_selector_mock.return_value = 2


        FlashCardRepo.retrieve_app_config()

        audio_column_selector_mock.assert_called_once()
        reading_column_selector_mock.assert_called_once()


    @patch("lexicon.repo.lexicon_repo.mw")
    def test_set_flash_card_due_date_in_embeded_application(
        self,
        main_window_mock: MagicMock
    ):
        """Outgoing arguement to set due date"""
        from fixtures.lexicon_fixtures import mock_flash_cards
        from lexicon.repo.lexicon_repo import FlashCardRepo

        FlashCardRepo.set_flash_card_due_date_in_embeded_application(
            5,
            mock_flash_cards(1)[0]
        )

        args, kwargs = main_window_mock.col.sched.set_due_date.call_args
        self.assertEqual(
            kwargs["days"],
            '5',
            msg="Outgoing arguement to set_due_date should be days_from_today"
        )

    @patch("lexicon.repo.lexicon_repo.mw")
    def test_set_flash_card_due_date_in_embeded_application_due_date_is_none(
        self,
        main_window_mock: MagicMock
    ):
        """AppConfig.audio_vocab_card_due_date of None
        does not call set_due_date on collection"""
        from fixtures.lexicon_fixtures import mock_flash_cards
        from lexicon.repo.lexicon_repo import FlashCardRepo


        FlashCardRepo.set_flash_card_due_date_in_embeded_application(
            None,
            mock_flash_cards(1)[0]
        )

        main_window_mock.col.sched.set_due_date.assert_not_called()