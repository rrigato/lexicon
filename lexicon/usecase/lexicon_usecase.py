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
    ) -> FlashCard:
        pass

    @abstractmethod
    def is_only_japanese_characters(self, str) -> bool:
        """raw user input validation for japanese characters"""
        pass

    @abstractmethod
    def make_mp3_for_anki(
        self,
        app_config: AppConfig,
        vocab_request: JapaneseVocabRequest
    ) -> str:
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

    @abstractmethod
    def set_flash_card_due_date_in_embeded_application(
        self,
        app_config: AppConfig,
        flash_card: FlashCard
    ) -> None:
        pass



