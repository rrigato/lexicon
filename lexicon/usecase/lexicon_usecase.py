from abc import ABC, abstractmethod
import logging

from lexicon.entities.lexicon_entity_model import AppConfig, JapaneseVocabRequest

class LearnJapaneseWordInterface(ABC):
    @abstractmethod
    def create_audio_vocab_card(
        self, create_vocab_request: JapaneseVocabRequest
    ) -> bool:
        pass

    @abstractmethod
    def create_reading_vocab_card(
        self, create_vocab_request: JapaneseVocabRequest
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

    logging.info(f"learn_japanese_word - Obtaining hiragana")

