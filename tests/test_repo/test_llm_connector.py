import json
import unittest
from unittest.mock import MagicMock, patch

from lexicon.entities.lexicon_constants import OPENAI_LLM_MODEL
from lexicon.entities.lexicon_entity_model import AudioConfig
from lexicon.repo.llm_connector import automatically_generate_definition, write_audio_to_file
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


    def test_load_hiragana_from_api(self):
        """
        GIVEN -
        - a populated AppConfig object
        and a populated JapaneseVocabRequest object
        WHEN -
            load_hiragana is called
        THEN -
            a str is returned with the hiragana text
            from an openai api call
        """
        pass

    @patch("lexicon.repo.llm_connector.urlopen")
    def test_write_audio_to_file(
        self,
        urlopen_mock: MagicMock
    ):
        """
        GIVEN -
            a app_config object
            a JapaneseVocabRequest object
            a AudioConfig object
        WHEN -
            write_audio_to_file is called
        THEN -
            an api is called to generate audio
            a file with the audio is written to the file system
        """
        urlopen_mock.__enter__.return_value.read.return_value = b"audio"


        write_audio_to_file(
            mock_app_config(),
            AudioConfig(
                file_name="mock_file.mp3",
                full_directory_path_to_write_file="mock/directory"
            ),
            mock_japanese_vocab_request()
        )




