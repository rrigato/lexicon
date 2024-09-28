import unittest


class TestLexiconEntry(unittest.TestCase):

    def test_orchestrate_japanese_vocab(self):
        """entry only invocation for creating jpaanese vocav"""
        from lexicon.entry.lexicon_entry import orchestrate_japanese_vocab

        '''TODO
            - invoke validate_japanese_vocab_request
            - invoke create_audio_vocab_card
            - invoke create_reading_vocab_card

        '''