import unittest


class TestLexiconEntityModel(unittest.TestCase):

    def test_message_board_post_bad_input(self):
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