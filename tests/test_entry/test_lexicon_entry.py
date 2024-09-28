import unittest


class TestLexiconEntry(unittest.TestCase):

    def test_orchestrate_japanese_vocab(self):
        """entry only invocation for creating jpaanese vocav"""
        from fixtures.lexicon_fixtures import mock_japanese_vocab_request
        from lexicon.entry.lexicon_entry import orchestrate_japanese_vocab

        '''TODO
            - invoke create_audio_vocab_card
            - invoke create_reading_vocab_card

        '''
        orchestrate_japanese_vocab(mock_japanese_vocab_request())