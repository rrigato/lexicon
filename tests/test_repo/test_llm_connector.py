import json
import unittest
from unittest.mock import MagicMock, patch

from lexicon.entities.lexicon_constants import OPENAI_LLM_MODEL
from lexicon.repo.llm_connector import automatically_generate_definition
from fixtures.lexicon_fixtures import mock_app_config, mock_japanese_vocab_request

class TestLlmConnector(unittest.TestCase):


    @patch("lexicon.repo.llm_connector.urlopen")
    def test_automatically_generate_definition(self, urlopen_mock: MagicMock):
        """
        GIVEN -
        - a populated AppConfig object
        WHEN -
        - automatically_generate_definition is called
        THEN -
        A JapaneseVocabRequest object is returned
        with word_definition populated from an openai api call
        """
        urlopen_mock.return_value.__enter__.return_value.read.return_value = json.dumps({
            "output": [
                {
                    "id": "rs_123",
                    "type": "reasoning",
                    "summary": []
                },
                {
                    "id": "msg_123",
                    "status": "completed",
                    "type": "message",
                    "content": [
                        {
                            "type": "output_text",
                            "text": "sample, definition"
                        }
                    ]
                }
            ]
        }).encode("utf-8")


        api_definition = automatically_generate_definition(
            mock_app_config(),
            mock_japanese_vocab_request(),
        )


        args, kwargs = urlopen_mock.call_args

        self.assertEqual(
            json.loads(args[0].data.decode("utf-8"))["model"],
            OPENAI_LLM_MODEL
        )
        self.assertIsNotNone(api_definition.word_definition)


