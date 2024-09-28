import unittest


class TestLexiconRepo(unittest.TestCase):

    def test_create_audio_vocab_card(self):
        """audio vocab card created for FlashCard"""
        from fixtures.lexicon_fixtures import mock_flash_cards
        from lexicon.repo.lexicon_repo import create_audio_vocab_card


        create_audio_vocab_card(
            mock_flash_cards(3)
        )
