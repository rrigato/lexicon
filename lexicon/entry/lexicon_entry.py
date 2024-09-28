
import logging

from lexicon.entities.lexicon_entity_model import JapaneseVocabRequest


def orchestrate_japanese_vocab(
    create_japanese_vocab_request: JapaneseVocabRequest
    ) -> None:
    """Provide a JapaneseVocabRequest and this interface
    will orchestrate the creation of a japanese audio and reading
    vocab card
    """
    logging.info(f"orchestrate_japanese_vocab - invocation begin")

    logging.info(f"orchestrate_japanese_vocab - invocation end")
    return(None)

