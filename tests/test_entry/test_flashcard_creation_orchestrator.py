import unittest
from unittest.mock import MagicMock, patch

from lexicon.entry.flashcard_creation_orchestrator import lookup_api_definition
from fixtures.lexicon_fixtures import mock_japanese_vocab_request, mock_app_config
class TestOrchestrateFlashCards(unittest.TestCase):

    @patch("lexicon.entry.flashcard_creation_orchestrator.automatically_generate_definition")
    @patch("lexicon.entry.flashcard_creation_orchestrator.FlashCardRepo")
    def test_lookup_api_definition(
        self,
        FlashCardRepo_mock: MagicMock,
        automatically_generate_definition_mock: MagicMock,
        ):
        """
        GIVEN
        - AppConfig.llm_api_key is populated
        - a populated vocab_word

        WHEN
            - lookup_api_definition is called
        THEN
            - automatically_generate_definition is called

        """
        app_config_mock = mock_app_config()
        FlashCardRepo_mock.retrieve_app_config.return_value = app_config_mock
        automatically_generate_definition_mock.return_value.word_definition = "Mock word definition"

        word_definition = lookup_api_definition(
            "輩"
        )

        self.assertEqual(
            word_definition,
            "Mock word definition"
        )