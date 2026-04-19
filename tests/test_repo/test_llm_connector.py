import json
import unittest
from unittest.mock import MagicMock, patch, mock_open

from lexicon.entities.lexicon_constants import (
    LLM_AUDIO_PROMPT,
    OPENAI_LLM_MODEL,
    OPENAI_AUDIO_SPEED,
    OPENAI_AUDIO_VOICE,
)
from lexicon.entities.lexicon_entity_model import AudioConfig, JapaneseVocabRequest
from lexicon.repo.llm_connector import _encoded_audio_post_data, automatically_generate_definition, write_audio_to_file
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
        payload = json.loads(args[0].data.decode("utf-8"))

        self.assertEqual(
            payload["model"],
            OPENAI_LLM_MODEL
        )
        self.assertIn("concise Japanese definitions", payload["input"])
        self.assertIn("simple Japanese vocabulary", payload["input"])
        self.assertIn("Provide a very concise Japanese definition", payload["input"])
        self.assertIsNotNone(api_definition.word_definition)


    def test_encoded_audio_post_data_uses_hiragana_as_spoken_input(self):
        """
        GIVEN -
        - a populated JapaneseVocabRequest object
        WHEN -
            _encoded_audio_post_data is called
        THEN -
            the audio payload uses the hiragana reading directly
            as the pronunciation target
        """
        payload = json.loads(
            _encoded_audio_post_data(
                mock_japanese_vocab_request()
            ).decode("utf-8")
        )

        self.assertEqual(payload["input"], "れい")
        self.assertEqual(payload["instructions"], LLM_AUDIO_PROMPT)
        self.assertEqual(payload["voice"], OPENAI_AUDIO_VOICE)
        self.assertEqual(payload["speed"], OPENAI_AUDIO_SPEED)

    def test_encoded_audio_post_data_prefers_hiragana_over_vocab(self):
        """
        GIVEN -
        - a JapaneseVocabRequest with kanji surface form and hiragana reading
        WHEN -
            _encoded_audio_post_data is called
        THEN -
            the request payload prefers the full hiragana reading
            when it is available
        """
        payload = json.loads(
            _encoded_audio_post_data(
                JapaneseVocabRequest(
                    vocab_to_create="輪廻",
                    hiragana_text="りんね",
                    word_definition="cycle of rebirth"
                )
            ).decode("utf-8")
        )

        self.assertEqual(payload["input"], "りんね")

    def test_encoded_audio_post_data_falls_back_to_original_text(self):
        """
        GIVEN -
        - a JapaneseVocabRequest without hiragana guidance
        WHEN -
            _encoded_audio_post_data is called
        THEN -
            the request payload falls back to the original text
        """
        payload = json.loads(
            _encoded_audio_post_data(
                JapaneseVocabRequest(
                    vocab_to_create="ありがとう",
                    word_definition="thank you"
                )
            ).decode("utf-8")
        )

        self.assertEqual(payload["input"], "ありがとう")

    @patch("builtins.open", new_callable=mock_open)
    @patch("lexicon.repo.llm_connector.urlopen")
    def test_write_audio_to_file(
        self,
        urlopen_mock: MagicMock,
        open_mock: MagicMock
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

        args, _kwargs = urlopen_mock.call_args
        payload = json.loads(args[0].data.decode("utf-8"))

        self.assertEqual(payload["input"], "れい")
        self.assertEqual(payload["instructions"], LLM_AUDIO_PROMPT)
        self.assertEqual(payload["voice"], OPENAI_AUDIO_VOICE)
        self.assertEqual(payload["speed"], OPENAI_AUDIO_SPEED)
        open_mock.assert_called_once()
