from abc import ABC, abstractmethod
import logging

from lexicon.entities.lexicon_entity_model import AppConfig, FlashCard, JapaneseVocabRequest

class LearnJapaneseWordInterface(ABC):
    @abstractmethod
    def create_audio_vocab_card(
        self,
        app_config: AppConfig,
        create_vocab_request: JapaneseVocabRequest
    ) -> FlashCard:
        pass

    @abstractmethod
    def create_reading_vocab_card(
        self,
        app_config: AppConfig,
        create_vocab_request: JapaneseVocabRequest
    ) -> bool:
        pass

    @abstractmethod
    def is_only_japanese_characters(self, str) -> bool:
        """raw user input validation for japanese characters"""
        pass

    @abstractmethod
    def populate_hiragana_text(
        self, initial_vocab_request: JapaneseVocabRequest
    ) -> JapaneseVocabRequest:
        pass

    @abstractmethod
    def retrieve_app_config(
        self
    ) -> AppConfig:
        pass



def learn_japanese_word(
        input_for_creating_flashcard: str,
        japanese_word_plugin: LearnJapaneseWordInterface
    )-> bool:
    """Usecase for storing a new japanese word in
    the spaced repetition system"""
    is_japanese = japanese_word_plugin.is_only_japanese_characters(
        input_for_creating_flashcard
    )

    if not is_japanese:
        logging.info(f"learn_japanese_word - Input is not Japanese: {input_for_creating_flashcard}")
        return(False)

    valid_vocab_request = JapaneseVocabRequest(
        vocab_to_create=input_for_creating_flashcard
    )
    logging.info(f"learn_japanese_word - Obtained valid_vocab_request")

    vocab_request_with_hiragana = japanese_word_plugin.populate_hiragana_text(
        valid_vocab_request
    )

    logging.info(f"learn_japanese_word - populated hiragana_text")

    runtime_config = japanese_word_plugin.retrieve_app_config()

    logging.info(f"learn_japanese_word - Obtained runtime_config")

    japanese_word_plugin.create_audio_vocab_card(
        runtime_config,
        vocab_request_with_hiragana
    )
    logging.info(f"learn_japanese_word - created audio card")

    japanese_word_plugin.create_reading_vocab_card(
        vocab_request_with_hiragana,
        runtime_config
    )
    logging.info(f"learn_japanese_word - created reading vocab card")


