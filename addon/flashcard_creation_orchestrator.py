import logging
from typing import Optional

from lexicon.entities.lexicon_entity_model import JapaneseVocabRequest
from lexicon.repo.llm_connector import automatically_generate_definition
from lexicon.repo.lexicon_repo import FlashCardRepo


def lookup_api_definition(vocab_word: str) -> str:
    '''Looks up a word definition using the LLM API


    Returns:
        The word definition from the API, or empty string
        if insufficient preconditions are met
    '''
    logging.info("lookup_api_definition - starting lookup for vocab_word: %s", vocab_word)

    if vocab_word == "":
        logging.info("lookup_api_definition - vocab_word is empty")
        return ""

    addon_app_config = FlashCardRepo.retrieve_app_config()

    if addon_app_config.llm_api_key is None:
        logging.info("lookup_api_definition - llm_api_key is None")
        return ""

    '''TODO - Allow user to validate definition before creating
    flash card'''
    return automatically_generate_definition(
        app_config=addon_app_config,
        japanese_vocab_request=JapaneseVocabRequest(
            vocab_to_create=vocab_word
        )
    ).word_definition
