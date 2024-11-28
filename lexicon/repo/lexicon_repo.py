import logging
import os
from logging.handlers import RotatingFileHandler
from time import strftime
from lexicon.entities.lexicon_entity_model import FlashCard
from aqt import mw

def create_audio_vocab_card(
    flash_card_to_create: FlashCard
    ) -> None:
    """creates an audio flash card in external system
    """
    logging.info(f"create_audio_vocab_card - invocation begin")

    logging.info(f"create_audio_vocab_card - invocation end")
    return(None)


def set_logger() -> None:
    """Set logger configuration
    https://github.com/abdnh/ankiutils/blob/master/src/ankiutils/log.py
    https://github.com/abdnh/anki-zim-reader/blob/master/src/consts.py#L4

    """
    lexicon_handler = RotatingFileHandler(
        filename=os.path.join(
            mw.addonManager.addonsFolder("lexicon"),
            "user_files",
            "lexicon_addon.log"
        ),
        maxBytes=3 * 1024 * 1024,
        backupCount=3
    )


    lexicon_handler.setFormatter(logging.Formatter(
                fmt="%(levelname)s | %(asctime)s.%(msecs)03d" +
                strftime("%z") + " | %(message)s",
                datefmt="%Y-%m-%dT%H:%M:%S",
            )
    )
    lexicon_handler.setLevel(logging.DEBUG)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(lexicon_handler)

    return(None)