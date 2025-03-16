
from copy import deepcopy
import random

from lexicon.entities.lexicon_entity_model import AppConfig, FlashCard, JapaneseVocabRequest



def _validate_drift(entity_instance) -> None:
    """Ensures that populated instance in
    fixture stays in sync with entity
    by making sure every attribute is populated
    """


    object_properties = [
        attr_name for attr_name in dir(entity_instance)
        if not attr_name.startswith("_")
    ]

    for object_property in object_properties:
        assert getattr(
            entity_instance, object_property) is not None,(
                f"\n_validate_drift - {object_property} " +
                "None for fixture"
            )
    return(None)

def mock_app_config(
    ) -> AppConfig:
    """Creates a mock AppConfig entity with all attributes populated"""

    mock_app_config = AppConfig()

    mock_app_config.audio_deck_name = "mock_audio_deck_name"
    mock_app_config.audio_note_template_name = "mock_audio_note_template_name"
    mock_app_config.audio_vocab_card_due_date = random.randint(0, 100)
    mock_app_config.audio_vocab_card_audio_column_number = random.randint(0, 10)
    mock_app_config.reading_deck_name = "mock_reading_deck_name"
    mock_app_config.reading_note_template_name = "mock_reading_note_template_name"
    mock_app_config.reading_vocab_card_due_date = random.randint(0, 100)

    _validate_drift(mock_app_config)

    return(deepcopy(mock_app_config))

def mock_flash_cards(
        number_of_entities: int
    ) -> list[FlashCard]:
    """Creates a list of mock FlashCard entities"""
    mock_entities_list = []

    for entity_num in range(number_of_entities):

        mock_entity = FlashCard()

        mock_entity.anki_card_id = entity_num
        mock_entity.anki_note_id = entity_num
        mock_entity.english_definition = (
            f"mock english_definition {entity_num}"
        )
        mock_entity.front_text = f"mock front_text {entity_num}"
        mock_entity.hiragana_text = (
            f"mock hiragana_text {entity_num}"
        )
        mock_entity.kanji_text = (
            f"mock kanji_text {entity_num}"
        )
        mock_entity.note_type = f"mock note_type {entity_num}"

        _validate_drift(mock_entity)

        mock_entities_list.append(mock_entity)

    return(deepcopy(mock_entities_list))



def mock_japanese_vocab_request(
    ) -> JapaneseVocabRequest:
    """Creates a list of mock JapaneseVocabRequest entities"""

    mock_japanese_vocab_request = JapaneseVocabRequest()

    mock_japanese_vocab_request.hiragana_text = "れい"
    mock_japanese_vocab_request.vocab_to_create = "例"

    _validate_drift(mock_japanese_vocab_request)

    return(deepcopy(mock_japanese_vocab_request))
