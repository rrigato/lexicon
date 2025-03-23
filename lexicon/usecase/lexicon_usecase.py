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


def audio_column_selector(
    app_config: AppConfig
) -> int:
    """validates
    app_config.audio_vocab_card_audio_column_number and
    returns the value it should be assigned

    Raises
    ------
        ValueError: if app_config.audio_vocab_card_audio_column_number
        is not in range appropriate to business rules of flash
        card application
    """
    if app_config.audio_vocab_card_audio_column_number is None:
        raise ValueError(
            "audio_vocab_card_audio_column_number must be set"
        )

    if app_config.audio_vocab_card_audio_column_number < 3:
        raise ValueError(
            "audio_vocab_card_audio_column_number must be greater than 2"
        )
    logging.info(
        "audio_column_selector - offsetting"
        " app_config.audio_vocab_card_audio_column_number from - "
        f"{app_config.audio_vocab_card_audio_column_number} to "
        f"{app_config.audio_vocab_card_audio_column_number - 1}")
    return app_config.audio_vocab_card_audio_column_number - 1

