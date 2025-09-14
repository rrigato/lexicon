import unittest
from unittest.mock import MagicMock, patch

from addon import _flash_card_input_prequisites
from fixtures.lexicon_fixtures import mock_japanese_vocab_request
class TestAddonInit(unittest.TestCase):

    @patch("aqt.qt.QInputDialog.getText")
    @patch("addon.lookup_api_definition")
    @patch("addon.learn_japanese_word")
    def test_main(
        self,
        learn_japanese_word_mock: MagicMock,
        lookup_api_definition_mock: MagicMock,
        getText_mock: MagicMock
    ):
        """external plugin calles clean architecture"""
        from addon import main
        getText_mock.side_effect = [
            ("救済", True),
            ("rescue", True)
        ]

        lookup_api_definition_mock.return_value = mock_japanese_vocab_request().word_definition
        learn_japanese_word_mock.return_value = None

        main()

        learn_japanese_word_mock.assert_called()
        lookup_api_definition_mock.assert_called_once()
        self.assertEqual(
            getText_mock.call_count,
            2,
            msg="getText should be called twice"
        )


    def test_flash_card_input_prequisites(self):
        """
        GIVEN -
            - user inputs an empty vocab word
        WHEN -
            - flash_card_input_prequisites is called
        THEN -
            - an info message is returned
        """
        vocab_word, word_definition, info_message = (
            _flash_card_input_prequisites(
                vocab_word="",
                word_definition=""
            )
        )
        self.assertEqual(vocab_word, "")
        self.assertEqual(word_definition, "")
        self.assertEqual(info_message, "Vocab word empty - no flash card created")


    @patch("aqt.qt.QMessageBox.information")
    @patch("addon.lookup_api_definition")
    @patch("aqt.qt.QInputDialog.getText")
    @patch("addon.learn_japanese_word")
    def test_main_unexpected_error(
        self,
        learn_japanese_word_mock: MagicMock,
        getText_mock: MagicMock,
        lookup_api_definition_mock: MagicMock,
        information_mock: MagicMock
    ):
        """text message is displayed to user on bad input"""
        from addon import main
        getText_mock.return_value = ("not a japanese character", True)
        lookup_api_definition_mock.return_value = mock_japanese_vocab_request().word_definition
        learn_japanese_word_mock.return_value = "Error message from input validation that we only accept japanese characters"


        main()

        learn_japanese_word_mock.assert_called()
        information_mock.assert_called()


    @patch.dict("sys.modules", {"lexicon.repo.lexicon_repo": None})
    @patch("os.sys.path")
    @patch("os.path")
    @patch("addon.mw")
    def test_configure_runtime_path(
        self,
        main_window_mock: MagicMock,
        os_path_mock: MagicMock,
        sys_path_mock: MagicMock
    ):
        """Not being able to import lexicon_repo should call sys path"""
        from addon import configure_runtime_path


        configure_runtime_path()

        sys_path_mock.insert.assert_called_once()
        main_window_mock.addonManager.addonsFolder.assert_called_once()