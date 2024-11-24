from abc import ABC, abstractmethod
import logging

class LearnJapaneseWordInterface(ABC):
    @abstractmethod
    def is_only_japanese_characters(self, str) -> bool:
        pass

def learn_japanese_word(
        input_for_creating_flashcard: str,
        japanese_word_plugin: LearnJapaneseWordInterface
    )-> bool:
    """Usecase for storing a new japanese word in
    the spaced repetition system"""
    is_japanese = japanese_word_plugin.is_only_japanese_characters("word")
    if not is_japanese:
        logging.info(f"learn_japanese_word - Input is not Japanese: {input_for_creating_flashcard}")
        return(False)
    