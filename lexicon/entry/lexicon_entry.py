
import logging

from lexicon.entities.lexicon_entity_model import JapaneseVocabRequest
from lexicon.repo.lexicon_repo import FlashCardRepo, create_audio_vocab_card


def orchestrate_japanese_vocab(
    japanese_vocab_request: JapaneseVocabRequest
    ) -> None:
    """Provide a JapaneseVocabRequest and this interface
    will orchestrate the creation of a japanese audio and reading
    vocab card
    """
    logging.info(f"orchestrate_japanese_vocab - invocation begin")
    create_audio_vocab_card(japanese_vocab_request)
    logging.info(f"orchestrate_japanese_vocab - invocation end")
    return(None)

def anki_input_handler():
    """Orchestrates invocation from raw external to clean architecture"""
    logging.info(f"anki_input_handler - invocation begin")

    flash_card_concrete_class = FlashCardRepo()

    logging.info(f"anki_input_handler - invocation end")
    return(None)