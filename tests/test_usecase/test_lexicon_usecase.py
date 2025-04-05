import unittest
from unittest.mock import MagicMock
from lexicon.usecase.lexicon_usecase import audio_column_selector

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

