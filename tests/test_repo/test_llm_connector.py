import json
import unittest
from unittest.mock import MagicMock, patch

from lexicon.entities.lexicon_constants import OPENAI_LLM_MODEL
from lexicon.repo.llm_connector import load_api_definition
from fixtures.lexicon_fixtures import mock_app_config, mock_japanese_vocab_request

class TestLlmConnector(unittest.TestCase):


    @patch("lexicon.repo.llm_connector.urlopen")
    def test_load_api_definition(self, urlopen_mock: MagicMock):
        """
        GIVEN -
        - a populated AppConfig object
        WHEN -
        - load_api_definition is called
        THEN -
        A JapaneseVocabRequest object is returned
        with word_definition populated from an openai api call
        """
        urlopen_mock.return_value.__enter__.return_value.read.return_value = json.dumps({
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": "sample, definition"
                    },
                    "finish_reason": "stop"
                }
            ]
        }).encode("utf-8")


        api_definition = load_api_definition(
            mock_app_config(),
            mock_japanese_vocab_request(),
        )


        args, kwargs = urlopen_mock.call_args

        self.assertEqual(
            json.loads(args[0].data.decode("utf-8"))["model"],
            OPENAI_LLM_MODEL
        )
        self.assertIsNotNone(api_definition.word_definition)