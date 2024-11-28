
import logging

from lexicon.entities.lexicon_entity_model import JapaneseVocabRequest
from lexicon.repo.lexicon_repo import create_audio_vocab_card


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

