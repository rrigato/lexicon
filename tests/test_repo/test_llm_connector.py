import unittest

from fixtures.lexicon_fixtures import mock_app_config, mock_japanese_vocab_request

class TestLlmConnector(unittest.TestCase):


    def test_load_api_definition(self):
        """
        GIVEN -
        - a populated AppConfig object
        WHEN -
        - load_api_definition is called
        THEN -
        A JapaneseVocabRequest object is returned
        with word_definition populated from an openai api call
        """
        from lexicon.repo.llm_connector import load_api_definition

        api_definition = load_api_definition(
            mock_app_config(),
            mock_japanese_vocab_request(),
        )


        self.assertIsNotNone(api_definition.word_definition)