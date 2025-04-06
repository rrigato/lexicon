
import logging
from typing import Optional

from lexicon.entities.lexicon_entity_model import AppConfig, FlashCard, JapaneseVocabRequest

from lexicon.repo.lexicon_repo import FlashCardRepo
from lexicon.usecase.lexicon_usecase import LearnJapaneseWordInterface

def learn_japanese_word(
        input_for_creating_flashcard: str,
        japanese_word_plugin: LearnJapaneseWordInterface,
        word_definition: str
    )-> Optional[str]:
    """Usecase for storing a new japanese word in
    the spaced repetition system"""
    is_japanese = japanese_word_plugin.is_only_japanese_characters(
        input_for_creating_flashcard
    )

    if not is_japanese:
        logging.info(f"learn_japanese_word - Input is not Japanese: {input_for_creating_flashcard}")
        return("Only Japanese characters are allowed")

    valid_vocab_request = JapaneseVocabRequest(
        vocab_to_create=input_for_creating_flashcard,
        word_definition=word_definition
    )
    logging.info(f"learn_japanese_word - Obtained valid_vocab_request")

    vocab_request_with_hiragana = japanese_word_plugin.populate_hiragana_text(
        valid_vocab_request
    )

    logging.info(f"learn_japanese_word - populated hiragana_text")

    runtime_config = japanese_word_plugin.retrieve_app_config()

    logging.info(f"learn_japanese_word - Obtained runtime_config")

    audio_flash_card = japanese_word_plugin.create_audio_vocab_card(
        runtime_config,
        vocab_request_with_hiragana
    )
    logging.info(f"learn_japanese_word - created audio card")

    reading_flash_card = japanese_word_plugin.create_reading_vocab_card(
        vocab_request_with_hiragana,
        runtime_config
    )
    logging.info(f"learn_japanese_word - created reading vocab card")



    japanese_word_plugin.set_flash_card_due_date_in_embeded_application(
        runtime_config.audio_vocab_card_due_date,
        audio_flash_card
    )

    japanese_word_plugin.set_flash_card_due_date_in_embeded_application(
        runtime_config.reading_vocab_card_due_date,
        reading_flash_card
    )
