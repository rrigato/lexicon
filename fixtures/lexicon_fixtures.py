
from copy import deepcopy

from lexicon.entities.lexicon_entity_model import FlashCard



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



def mock_flash_cards(
        number_of_entities: int
    ) -> list[FlashCard]:
    """Creates a list of mock FlashCard entities"""
    mock_entities_list = []

    for entity_num in range(number_of_entities):

        mock_entity = FlashCard()

        mock_entity.english_defintion = (
            f"mock english_defintion {entity_num}"
        )
        mock_entity.front_text = f"mock front_text {entity_num}"
        mock_entity.note_type = f"mock note_type {entity_num}"

        _validate_drift(mock_entity)

        mock_entities_list.append(mock_entity)

    return(deepcopy(mock_entities_list))
