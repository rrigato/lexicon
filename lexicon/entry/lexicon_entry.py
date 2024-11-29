
import logging

from lexicon.repo.lexicon_repo import FlashCardRepo

def orchestrate_japanese_vocab() -> None:
    """Orchestrate the creation of a Japanese vocab card
    """
    logging.info(f"orchestrate_japanese_vocab - invocation begin")

    flash_card_concrete_class = FlashCardRepo()

    logging.info(f"orchestrate_japanese_vocab - invocation end")
    return(None)