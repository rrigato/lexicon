import unittest
from unittest.mock import MagicMock, patch

from fixtures.lexicon_fixtures import mock_japanese_vocab_request
class TestAddonInit(unittest.TestCase):

    @patch("aqt.qt.QInputDialog.getText")
    @patch("addon.learn_japanese_word")
    def test_main(
        self,
        learn_japanese_word_mock: MagicMock,
        getText_mock: MagicMock
    ):
        """external plugin calles clean architecture"""
        from addon import main
        getText_mock.return_value = ("救済", True)


        main()

        learn_japanese_word_mock.assert_called()


