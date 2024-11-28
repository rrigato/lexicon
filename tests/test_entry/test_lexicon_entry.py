import unittest
from unittest.mock import MagicMock, patch


class TestLexiconEntry(unittest.TestCase):

    @patch("lexicon.entry.lexicon_entry.create_audio_vocab_card")
    def test_orchestrate_japanese_vocab(
            self,
            mock_create_audio_vocab_card: MagicMock):
        """entry only invocation for creating jpaanese vocav"""
        from fixtures.lexicon_fixtures import mock_japanese_vocab_request
        from lexicon.entry.lexicon_entry import orchestrate_japanese_vocab

        mock_create_audio_vocab_card.return_value = None

        '''TODO
            - invoke create_reading_vocab_card
        '''
        orchestrate_japanese_vocab(mock_japanese_vocab_request())

        mock_create_audio_vocab_card.assert_called_once()