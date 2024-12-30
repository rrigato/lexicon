import unittest


class TestLexiconEntityModel(unittest.TestCase):

    def test_app_config_bad_input(self):
        """invalid datatypes for entity raise TypeError"""
        from fixtures.lexicon_fixtures import mock_app_config
        from lexicon.entities.lexicon_entity_model import AppConfig

        mock_invalid_types = [
            set(["a", "b"]),
            (1, 2, 3),
            {},
            ["a", "list"]
        ]

        object_properties = [
            attr_name for attr_name in dir(AppConfig())
            if not attr_name.startswith("_")
        ]
        for mock_invalid_type in mock_invalid_types:
            with self.subTest(mock_invalid_type=mock_invalid_type):

                mock_entity = AppConfig()



                for object_property in object_properties:
                    with self.assertRaises(TypeError, msg=f"check property - {object_property}"):
                        setattr(
                            mock_entity,
                            object_property,
                            mock_invalid_type
                        )

        isinstance(mock_app_config(), AppConfig)


    def test_flash_card_bad_input(self):
        """invalid datatypes for entity raise TypeError"""
        from fixtures.lexicon_fixtures import mock_flash_cards
        from lexicon.entities.lexicon_entity_model import FlashCard

        mock_invalid_types = [
            set(["a", "b"]),
            (1, 2, 3),
            {},
            ["a", "list"]
        ]

        object_properties = [
            attr_name for attr_name in dir(FlashCard())
            if not attr_name.startswith("_")
        ]
        for mock_invalid_type in mock_invalid_types:
            with self.subTest(mock_invalid_type=mock_invalid_type):

                mock_entity = FlashCard()



                for object_property in object_properties:
                    with self.assertRaises(TypeError):
                        setattr(
                            mock_entity,
                            object_property,
                            mock_invalid_type
                        )

        mock_flash_cards(3)


    def test_japanese_vocab_request(self):
        """invalid datatypes for entity raise TypeError"""
        from fixtures.lexicon_fixtures import mock_japanese_vocab_request
        from lexicon.entities.lexicon_entity_model import JapaneseVocabRequest

        mock_invalid_types = [
            set(["a", "b"]),
            (1, 2, 3),
            {},
            1,
            ["a", "list"]
        ]

        object_properties = [
            attr_name for attr_name in dir(JapaneseVocabRequest())
            if not attr_name.startswith("_")
        ]
        for mock_invalid_type in mock_invalid_types:
            with self.subTest(mock_invalid_type=mock_invalid_type):

                mock_entity = JapaneseVocabRequest()



                for object_property in object_properties:
                    with self.assertRaises(TypeError):
                        setattr(
                            mock_entity,
                            object_property,
                            mock_invalid_type
                        )

        isinstance(mock_japanese_vocab_request(), JapaneseVocabRequest)