import unittest
from unittest.mock import MagicMock
from lexicon.usecase.lexicon_usecase import audio_column_selector, reading_column_selector

from fixtures.lexicon_fixtures import mock_app_config, mock_japanese_vocab_request
class TestLexiconUsecase(unittest.TestCase):
    def test_audio_column_selector(self):
        """
        GIVEN -
        - an invalid audio_vocab_card_audio_column_number
        WHEN -
        - the audio_column_selector method is called
        THEN -
        - a ValueError is raised
        """
        invalid_config_0 = mock_app_config()
        invalid_config_1 = mock_app_config()
        invalid_config_2 = mock_app_config()


        invalid_config_0.audio_vocab_card_audio_column_number = 2
        invalid_config_1.audio_vocab_card_audio_column_number = None
        invalid_config_2.audio_vocab_card_audio_column_number = -1

        invalid_app_configs = [
            invalid_config_0,
            invalid_config_1,
            invalid_config_2
        ]

        for app_config in invalid_app_configs:
            with self.assertRaises(ValueError):
                audio_column_selector(app_config)

    def test_reading_column_selector(self):
        """
        GIVEN -
        - an invalid reading_vocab_card_audio_column_number
        WHEN -
        - the reading_column_selector method is called
        THEN -
        - a ValueError is raised
        """
        invalid_config_0 = mock_app_config()
        invalid_config_1 = mock_app_config()
        invalid_config_2 = mock_app_config()

        invalid_config_0.reading_vocab_card_audio_column_number = 2
        invalid_config_1.reading_vocab_card_audio_column_number = None
        invalid_config_2.reading_vocab_card_audio_column_number = -1

        invalid_app_configs = [
            invalid_config_0,
            invalid_config_1,
            invalid_config_2
        ]

        for app_config in invalid_app_configs:
            with self.assertRaises(ValueError):
                reading_column_selector(app_config)

    def test_reading_column_selector_returns_correct_value(self):
        """
        GIVEN -
        - a valid reading_vocab_card_audio_column_number
        WHEN -
        - the reading_column_selector method is called
        THEN -
        - the offset columnvalue is returned
        """
        valid_config = mock_app_config()
        valid_config.reading_vocab_card_audio_column_number = 3

        self.assertEqual(reading_column_selector(valid_config), 2)
