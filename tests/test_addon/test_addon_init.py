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
        learn_japanese_word_mock.return_value = None


        main()

        learn_japanese_word_mock.assert_called()
        self.assertEqual(
            getText_mock.call_count,
            2,
            msg="getText should be called twice"
        )


    @patch("aqt.qt.QMessageBox.information")
    @patch("aqt.qt.QInputDialog.getText")
    @patch("addon.learn_japanese_word")
    def test_main_unexpected_error(
        self,
        learn_japanese_word_mock: MagicMock,
        getText_mock: MagicMock,
        information_mock: MagicMock
    ):
        """text message is displayed to user on bad input"""
        from addon import main
        getText_mock.return_value = ("not a japanese character", True)
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